import os

import pytest
from silurian import AsyncEarth, Earth

API_KEY_ENV = "SILURIAN_EARTH_API_KEY"

@pytest.mark.skipif(
    not os.getenv(API_KEY_ENV),
    reason=f"Skipping live API tests. {API_KEY_ENV} environment variable not set"
)
def test_sync_client() -> None:
    api_key = os.environ[API_KEY_ENV] 
    client = Earth(
        api_key=api_key
    )
    assert isinstance(client, Earth)
    response_daily = client.weather.forecast.daily(
        latitude=47.6061,
        longitude=-122.3328
    )
    assert response_daily is not None

    response_hourly = client.weather.forecast.hourly(
        latitude=47.6061,
        longitude=-122.3328
    )
    assert response_hourly is not None

@pytest.mark.skipif(
    not os.getenv(API_KEY_ENV),
    reason=f"Skipping live API tests. {API_KEY_ENV} environment variable not set"
)
@pytest.mark.asyncio
async def test_weather_forecast_async_daily() -> None:
    api_key = os.environ[API_KEY_ENV] 
    client = AsyncEarth(api_key=api_key)
    
    # Using Seattle coordinates as test data
    response = await client.weather.forecast.daily(
        latitude=47.6061,
        longitude=-122.3328
    )
    assert response is not None

@pytest.mark.skipif(
    not os.getenv(API_KEY_ENV),
    reason=f"Skipping live API tests. {API_KEY_ENV} environment variable not set"
)
@pytest.mark.asyncio
async def test_weather_forecast_async_hourly() -> None:
    api_key = os.environ[API_KEY_ENV] 
    client = AsyncEarth(api_key=api_key)
    
    # Using Seattle coordinates as test data
    response = await client.weather.forecast.hourly(
        latitude=47.6061,
        longitude=-122.3328
    )
    assert response is not None    