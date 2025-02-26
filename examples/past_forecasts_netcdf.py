import asyncio
from datetime import datetime, timedelta
import time
import json
import traceback
from typing import List, Optional, Set
import os

import pandas as pd
import numpy as np
import xarray as xr
from silurian import AsyncEarth
from tqdm import tqdm

API_KEY = os.environ["SILURIAN_API_KEY"]
MAX_CONCURRENT_REQUESTS = 200  # Maximum concurrent API requests
RATE_LIMIT_PER_MINUTE = 1200   # API rate limit (requests per minute)
CHECKPOINT_FILE = "status.json"

######
# Takes a csv of locations as input
#
# locations.csv:
#
# latitude, longitude
# 32.45, -122.45
#
# Usage: python past_forecasts_netcdf.py --csv locations.csv --start-date 2023-01-01 --end-date 2023-12-31 --output file.nc

# Global state for request tracking
class RequestTracker:
    def __init__(self):
        self.count = 0
        self.start_time = time.time()
        
    def increment(self):
        self.count += 1
        
    def reset(self):
        self.count = 0
        self.start_time = time.time()
        
    def get_rate(self) -> float:
        elapsed = time.time() - self.start_time
        if elapsed > 0:
            return (self.count / elapsed) * 60
        return 0
    
request_tracker = RequestTracker()

async def fetch_forecast_window(
    client: AsyncEarth, 
    latitude: float, 
    longitude: float, 
    start_time: datetime,
    idx: int
) -> Optional[pd.DataFrame]:
    """
    Fetch forecast for a specific time window
    
    Args:
        client: The AsyncEarth client
        latitude: Location latitude
        longitude: Location longitude
        start_time: Start time for the forecast
        idx: Plant index
        
    Returns:
        DataFrame with forecast data or None if there was an error
    """
    # Track request count
    request_tracker.increment()
    
    # Make sure start_time is a datetime object
    if isinstance(start_time, str):
        try:
            start_time = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
        except ValueError:
            start_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
    
    try:
        # Make the API request
        response = await client.weather.past.forecast.hourly(
            latitude=latitude,
            longitude=longitude,
            time=start_time,
            timezone="utc",
        )
        
        # Process the response
        forecast_data = []
        for hour in response.hourly:
            # Create a data dictionary with metadata
            data_dict = {
                "init_time": response.forecast_time,
                "timestamp": hour.timestamp,
                "location_index": idx,
                "latitude": latitude,
                "longitude": longitude,
                # Weather variables from the HourlyConditions class
                "temperature": getattr(hour, "temperature", None),
                "precipitation_accumulation": getattr(hour, "precipitation_accumulation", None),
                "precipitation_probability": getattr(hour, "precipitation_probability", None),
                #"precipitation_type": getattr(hour, "precipitation_type", None),
                "snowfall_accumulation": getattr(hour, "snowfall_accumulation", None),
                "cloud_cover": getattr(hour, "cloud_cover", None),
                "humidity": getattr(hour, "humidity", None),
                "wind_speed": getattr(hour, "wind_speed", None),
                "wind_direction": getattr(hour, "wind_direction", None),
                "dewpoint_temperature": getattr(hour, "dewpoint_temperature", None),
                "pressure": getattr(hour, "pressure", None),
                "downward_solar_radiation": getattr(hour, "downward_solar_radiation", None),
                "wind_speed_100m": getattr(hour, "wind_speed_100_m", None),
                "wind_direction_100m": getattr(hour, "wind_direction_100_m", None),
                "feels_like_temperature": getattr(hour, "feels_like_temperature", None),
                #"weather_code": getattr(hour, "weather_code", None),
                "global_horizontal_irradiation": getattr(hour, "global_horizontal_irradiation", None),
                "direct_normal_irradiation": getattr(hour, "direct_normal_irradiation", None),
                "diffuse_horizontal_irradiation": getattr(hour, "diffuse_horizontal_irradiation", None)
            }
            
            # Remove None values to save space
            data_dict = {k: v for k, v in data_dict.items() if v is not None}
            
            forecast_data.append(data_dict)
        
        return pd.DataFrame(forecast_data)
        
    except Exception as e:
        print(f"API request failed for location {idx} at {start_time}: {str(e)}")
        return None
    
async def process_location(
    client: AsyncEarth, 
    latitude: float, 
    longitude: float, 
    idx: int,
    start_date: datetime,
    end_date: datetime,
    forecast_interval: int = 6
) -> Optional[pd.DataFrame]:
    """
    Process all forecast windows for a single location
    
    Args:
        client: The AsyncEarth client
        latitude: Location latitude
        longitude: Location longitude
        idx: Location index
        start_date: Start date for forecasts
        end_date: End date for forecasts
        forecast_interval: Hours between forecast init times
        
    Returns:
        DataFrame with all forecast data or None if there was an error
    """
    # Generate list of forecast init times
    forecast_times = []
    current_time = start_date
    while current_time <= end_date:
        forecast_times.append(current_time)
        current_time += timedelta(hours=forecast_interval)
    
    print(f"Location {idx}: Processing {len(forecast_times)} forecast init times from {start_date} to {end_date}")
    
    location_dfs = []
    
    # Process each forecast time
    for start_time in forecast_times:
        try:
            df = await fetch_forecast_window(client, latitude, longitude, start_time, idx)
            if df is not None and not df.empty:
                location_dfs.append(df)
                
            # Add a small delay to avoid overwhelming the API
            # Calculate delay based on rate limit
            target_delay = 60 / (RATE_LIMIT_PER_MINUTE)
            await asyncio.sleep(target_delay)
                
        except Exception as e:
            print(f"Failed to fetch data for location {idx} at {start_time}: {e}")
    
    # Combine all dataframes for this location
    if location_dfs:
        result_df = pd.concat(location_dfs).drop_duplicates(subset=['timestamp', 'init_time'])
        print(f"Location {idx}: Collected {len(result_df)} hourly data points across {len(location_dfs)} forecasts")
        return result_df
    
    return None

def create_netcdf_from_dataframes(dataframes: List[pd.DataFrame], output_file: str) -> bool:
    """
    Convert a list of dataframes to a single NetCDF file
    
    Args:
        dataframes: List of dataframes with forecast data
        output_file: Path to output NetCDF file
        
    Returns:
        True if successful, False otherwise
    """
    if not dataframes:
        print("No data to write")
        return False
        
    try:
        # Combine all dataframes
        combined_df = pd.concat(dataframes, ignore_index=True)
        print(f"Creating NetCDF file with {len(combined_df)} total data points")
        
        # Determine unique values for dimensions
        locations = combined_df['location_index'].unique()
        timestamps = sorted(combined_df['timestamp'].unique())
        init_times = sorted(combined_df['init_time'].unique())
        
        # Identify all data variables (excluding metadata columns)
        metadata_cols = {'location_index', 'latitude', 'longitude', 'init_time', 'timestamp'}
        data_variables = [col for col in combined_df.columns if col not in metadata_cols]
        
        print(f"Found {len(data_variables)} data variables to include in NetCDF")
        
        # Create mapping dictionaries for faster lookups
        location_idx_map = {loc: i for i, loc in enumerate(locations)}
        init_time_idx_map = {pd.Timestamp(t): i for i, t in enumerate(init_times)}
        timestamp_idx_map = {pd.Timestamp(t): i for i, t in enumerate(timestamps)}
        
        # Extract lat/lon values for each location
        lat_values = np.array([combined_df[combined_df['location_index'] == loc]['latitude'].iloc[0] for loc in locations])
        lon_values = np.array([combined_df[combined_df['location_index'] == loc]['longitude'].iloc[0] for loc in locations])
        
        # Create variable dictionaries for xarray Dataset
        data_vars = {}
        
        # Create arrays for each variable and fill with data
        for var_name in data_variables:
            # Skip string/categorical columns for NetCDF
            if combined_df[var_name].dtype == 'object' or combined_df[var_name].dtype == 'string':
                print(f"Skipping string variable '{var_name}' as NetCDF doesn't handle these well")
                continue
                
            # Initialize empty array for this variable
            var_data = np.full((len(locations), len(init_times), len(timestamps)), np.nan)
            
            # Fill the data array
            for _, row in combined_df.iterrows():
                if var_name in row and pd.notna(row[var_name]):
                    loc_idx = location_idx_map[row['location_index']]
                    init_idx = init_time_idx_map[pd.Timestamp(row['init_time'])]
                    time_idx = timestamp_idx_map[pd.Timestamp(row['timestamp'])]
                    var_data[loc_idx, init_idx, time_idx] = row[var_name]
            
            # Add to data_vars dictionary
            data_vars[var_name] = (['location', 'init_time', 'time'], var_data)
        
        # Add lat/lon to data_vars
        data_vars['latitude'] = (['location'], lat_values)
        data_vars['longitude'] = (['location'], lon_values)
        
        # Create xarray dataset
        ds = xr.Dataset(
            data_vars=data_vars,
            coords={
                'location': locations,
                'init_time': init_times,
                'time': timestamps,
            },
            attrs={
                'description': 'Weather forecast data',
                'created': datetime.now().isoformat(),
                'source': 'Silurian AsyncEarth API',
            }
        )
        
        # Add variable attributes where known
        var_attributes = {
            'temperature': {'units': 'celsius', 'long_name': 'Temperature at 2m'},
            'precipitation_accumulation': {'units': 'mm', 'long_name': 'Precipitation Accumulation'},
            'precipitation_probability': {'units': '%', 'long_name': 'Precipitation Probability'},
            'snowfall_accumulation': {'units': 'mm', 'long_name': 'Snowfall Accumulation'},
            'cloud_cover': {'units': '%', 'long_name': 'Cloud Cover'},
            'humidity': {'units': '%', 'long_name': 'Relative Humidity'},
            'wind_speed': {'units': 'm/s', 'long_name': 'Wind Speed at 10m'},
            'wind_direction': {'units': 'degrees', 'long_name': 'Wind Direction at 10m'},
            'dewpoint_temperature': {'units': 'celsius', 'long_name': 'Dewpoint Temperature'},
            'pressure': {'units': 'hPa', 'long_name': 'Surface Pressure'},
            'downward_solar_radiation': {'units': 'W/m^2', 'long_name': 'Downward Solar Radiation'},
            'wind_speed_100m': {'units': 'm/s', 'long_name': 'Wind Speed at 100m'},
            'wind_direction_100m': {'units': 'degrees', 'long_name': 'Wind Direction at 100m'},
            'feels_like_temperature': {'units': 'celsius', 'long_name': 'Feels Like Temperature'},
            'global_horizontal_irradiation': {'units': 'kW/m^2', 'long_name': 'Global Horizontal Irradiation'},
            'direct_normal_irradiation': {'units': 'kW/m^2', 'long_name': 'Direct Normal Irradiation'},
            'diffuse_horizontal_irradiation': {'units': 'kW/m^2', 'long_name': 'Diffuse Horizontal Irradiation'},
            'latitude': {'units': 'degrees_north', 'long_name': 'Latitude'},
            'longitude': {'units': 'degrees_east', 'long_name': 'Longitude'}
        }
        
        # Add attributes to variables where we have predefined attributes
        for var_name in ds.data_vars:
            if var_name in var_attributes:
                ds[var_name].attrs = var_attributes[var_name]
        
        # Save to NetCDF file
        ds.to_netcdf(output_file)
        print(f"Successfully wrote NetCDF file to {output_file}")
        
        return True
    except Exception as e:
        print(f"Error creating NetCDF file: {e}")
        traceback.print_exc()
        return False
    
async def monitor_request_rate() -> None:
    """
    Monitor and log the current API request rate
    """
    global request_tracker
    
    while True:
        await asyncio.sleep(10)  # Update every 10 seconds
        rate = request_tracker.get_rate()
        print(f"\n--- MONITORING: Made {request_tracker.count} requests in "
              f"{time.time() - request_tracker.start_time:.1f} seconds "
              f"({rate:.1f} requests/minute) ---\n")

class LocationProcessor:
    """Manages processing of locations with proper concurrency control"""
    
    def __init__(
        self, 
        client: AsyncEarth,
        max_concurrent: int = MAX_CONCURRENT_REQUESTS
    ):
        self.client = client
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.completed_indices: Set[int] = set()
        
    async def process_location_with_semaphore(
        self, 
        latitude: float, 
        longitude: float, 
        idx: int,
        start_date: datetime,
        end_date: datetime
    ) -> Optional[pd.DataFrame]:
        """Process a location with semaphore control"""
        async with self.semaphore:
            return await process_location(
                self.client, 
                latitude, 
                longitude, 
                idx, 
                start_date, 
                end_date
            )
    
    async def load_checkpoint(self) -> None:
        """Load checkpoint data to resume from previous run"""
        try:
            with open(CHECKPOINT_FILE, 'r') as f:
                checkpoint = json.load(f)
                self.completed_indices = set(checkpoint.get('completed_indices', []))
                print(f"Loaded checkpoint with {len(self.completed_indices)} completed locations")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No valid checkpoint found, starting from beginning")
            self.completed_indices = set()
    
    async def save_checkpoint(self) -> None:
        """Save checkpoint data to resume from later"""
        try:
            with open(CHECKPOINT_FILE, 'w') as f:
                json.dump({
                    'completed_indices': list(self.completed_indices)
                }, f)
        except Exception as e:
            print(f"Error saving checkpoint: {e}")
    
    async def process_all_locations(
        self, 
        locations_df: pd.DataFrame, 
        start_date: datetime,
        end_date: datetime,
        batch_size: int = 20
    ) -> List[pd.DataFrame]:
        """
        Process all locations in batches
        
        Args:
            locations_df: DataFrame with location information
            start_date: Start date for forecasts
            end_date: End date for forecasts
            batch_size: Number of locations to process in each batch
            
        Returns:
            List of dataframes with forecast data
        """
        # Filter out already completed locations
        if self.completed_indices:
            remaining_df = locations_df[~locations_df.index.isin(self.completed_indices)]
            print(f"Remaining locations to process: {len(remaining_df)} of {len(locations_df)}")
        else:
            remaining_df = locations_df
        
        # Process in batches
        total_locations = len(remaining_df)
        total_batches = (total_locations + batch_size - 1) // batch_size
        
        all_results = []
        
        for batch_idx in range(total_batches):
            start_idx = batch_idx * batch_size
            end_idx = min(start_idx + batch_size, total_locations)
            batch_df = remaining_df.iloc[start_idx:end_idx]
            
            print(f"\nProcessing batch {batch_idx+1}/{total_batches} "
                  f"(locations {start_idx}-{end_idx}, {len(batch_df)} locations)")
            
            # Create tasks for all locations in this batch
            tasks = []
            for idx, row in batch_df.iterrows():
                task = asyncio.create_task(
                    self.process_location_with_semaphore(
                        row["latitude"],
                        row["longitude"],
                        idx,
                        start_date,
                        end_date
                    )
                )
                tasks.append((idx, task))
            
            # Process results as they complete
            batch_results = []
            newly_completed = set()
            
            with tqdm(total=len(tasks)) as pbar:
                for idx, task in tasks:
                    try:
                        result = await task
                        
                        if result is not None and not result.empty:
                            batch_results.append(result)
                            newly_completed.add(idx)
                    except Exception as e:
                        print(f"Error processing location {idx}: {e}")
                    
                    pbar.update(1)
            
            # Add batch results to all results
            all_results.extend(batch_results)
            self.completed_indices.update(newly_completed)
            await self.save_checkpoint()
            
            # Brief pause between batches
            if batch_idx < total_batches - 1:
                print("Pausing between batches...")
                await asyncio.sleep(2)
        
        print(f"All batches complete. Processed {len(self.completed_indices)} locations in total.")
        return all_results
    
async def main() -> None:
    """Main function to run the weather forecast data collection process"""
    # Parse command-line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Fetch weather forecast data and save as NetCDF')
    parser.add_argument('--csv', type=str, required=True, help='Path to CSV file with latitude/longitude data')
    parser.add_argument('--start-date', type=str, required=True, help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', type=str, required=True, help='End date (YYYY-MM-DD)')
    parser.add_argument('--output', type=str, default='forecast_data.nc', help='Output NetCDF file')
    parser.add_argument('--batch-size', type=int, default=20, help='Number of locations to process in each batch')
    args = parser.parse_args()
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or '.', exist_ok=True)
    
    # Initialize client
    client = AsyncEarth(api_key=API_KEY)

    # Parse dates
    try:
        start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
        end_date = datetime.strptime(args.end_date, "%Y-%m-%d") + timedelta(days=1) - timedelta(seconds=1)
    except ValueError as e:
        print(f"Error parsing dates: {e}")
        print("Please use YYYY-MM-DD format for dates")
        return        
    
    # Start monitoring task
    monitor_task = asyncio.create_task(monitor_request_rate())    
    try:
        # Read locations from CSV file
        print(f"Reading locations from {args.csv}...")
        try:
            locations_df = pd.read_csv(args.csv)
            
            # Validate CSV format
            required_columns = ['latitude', 'longitude']
            missing_columns = [col for col in required_columns if col not in locations_df.columns]
            if missing_columns:
                print(f"Error: CSV file missing required columns: {missing_columns}")
                print(f"Available columns: {', '.join(locations_df.columns)}")
                return
                
            print(f"Found {len(locations_df)} locations in CSV file")
            
            # Reset index if not already numeric
            if not isinstance(locations_df.index, pd.RangeIndex):
                locations_df = locations_df.reset_index()
                
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return
        
        # Initialize location processor
        processor = LocationProcessor(client)
        
        # Load checkpoint data
        await processor.load_checkpoint()
        
        # Process all locations
        all_results = await processor.process_all_locations(
            locations_df, 
            start_date, 
            end_date,
            batch_size=args.batch_size
        )            
        print(f"First batch processing completed. Checking for any available data to analyze structure...")
        if all_results and len(all_results) > 0:
            # Check the first DataFrame to see what variables we've collected
            first_df = all_results[0]
            print("\nAvailable variables in the forecast data:")
            for col in first_df.columns:
                if col not in ['location_index', 'latitude', 'longitude', 'init_time', 'timestamp']:
                    print(f"  - {col}")
        
        # Create NetCDF file from results
        if all_results:
            create_netcdf_from_dataframes(all_results, args.output)
        else:
            print("No data collected, cannot create NetCDF file")
    except Exception as e:
        print(f"Unexpected error in main process: {e}")
        traceback.print_exc()
    finally:
        # Clean up monitoring task
        monitor_task.cancel()
        try:
            await monitor_task
        except asyncio.CancelledError:
            pass

if __name__ == "__main__":
    print(f"Starting forecast data collection at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    start_time = time.time()
    # Set up custom event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        # Run the main process
        loop.run_until_complete(main())
        
        # Report completion
        elapsed = time.time() - start_time
        print(f"Completed in {elapsed:.2f} seconds ({elapsed/60:.2f} minutes)")
        print(f"Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user")
        
        # Cancel all running tasks
        tasks = asyncio.all_tasks(loop)
        for task in tasks:
            task.cancel()
        
        # Allow tasks to finish cancellation
        group = asyncio.gather(*tasks, return_exceptions=True)
        loop.run_until_complete(group)
    except Exception as e:
        print(f"Process failed with error: {e}")
        traceback.print_exc()
    finally:
        # Close the event loop
        loop.close()
        print("Process exited cleanly")            
        