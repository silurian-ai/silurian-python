# Reference
## Cyclones
<details><summary><code>client.cyclones.<a href="src/silurian/cyclones/client.py">query_forecasts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query the available cyclone forecasts for a particular time
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.cyclones.query_forecasts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**time:** `typing.Optional[dt.datetime]` — *Default value: (current time) - Default time zone: UTC*
    
</dd>
</dl>

<dl>
<dd>

**min_storm_category:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[ModelName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cyclones.<a href="src/silurian/cyclones/client.py">get_forecast_track</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get cyclone tracks in GeoJSON (MF-GeoJSON) format
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.cyclones.get_forecast_track(storm_id='storm_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**storm_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[dt.datetime]` — *Default value: (current time) - Default time zone: UTC*
    
</dd>
</dl>

<dl>
<dd>

**max_lead_time:** `typing.Optional[str]` — *Value must be > P0D*
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[ModelName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cyclones.<a href="src/silurian/cyclones/client.py">get_forecast_cone</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get cyclone forecast cone in GeoJSON format
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.cyclones.get_forecast_cone(storm_id='storm_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**storm_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[dt.datetime]` — *Default value: (current time) - Default time zone: UTC*
    
</dd>
</dl>

<dl>
<dd>

**max_lead_time:** `typing.Optional[str]` — *Value must be > P0D*
    
</dd>
</dl>

<dl>
<dd>

**smooth_cone:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[ModelName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Cyclones Forecasts
<details><summary><code>client.cyclones.forecasts.<a href="src/silurian/cyclones/forecasts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query the available cyclone forecasts for a particular time
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.cyclones.forecasts.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**time:** `typing.Optional[dt.datetime]` — *Default value: (current time) - Default time zone: UTC*
    
</dd>
</dl>

<dl>
<dd>

**min_storm_category:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[ModelName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cyclones.forecasts.<a href="src/silurian/cyclones/forecasts/client.py">track</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get cyclone tracks in GeoJSON (MF-GeoJSON) format
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.cyclones.forecasts.track(storm_id='storm_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**storm_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[dt.datetime]` — *Default value: (current time) - Default time zone: UTC*
    
</dd>
</dl>

<dl>
<dd>

**max_lead_time:** `typing.Optional[str]` — *Value must be > P0D*
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[ModelName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cyclones.forecasts.<a href="src/silurian/cyclones/forecasts/client.py">cone</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get cyclone forecast cone in GeoJSON format
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.cyclones.forecasts.cone(storm_id='storm_id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**storm_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[dt.datetime]` — *Default value: (current time) - Default time zone: UTC*
    
</dd>
</dl>

<dl>
<dd>

**max_lead_time:** `typing.Optional[str]` — *Value must be > P0D*
    
</dd>
</dl>

<dl>
<dd>

**smooth_cone:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[ModelName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Weather Forecast
<details><summary><code>client.weather.forecast.<a href="src/silurian/weather/forecast/client.py">daily</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get daily weather forecast for a specific location
Only allowing local timezone aggregations for now since
it is unclear how exactly users will understand "UTC".
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.weather.forecast.daily(latitude=47.6061, longitude=-122.3328, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**latitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[typing.Literal["local"]]` 
    
</dd>
</dl>

<dl>
<dd>

**units:** `typing.Optional[Units]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.weather.forecast.<a href="src/silurian/weather/forecast/client.py">hourly</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get hourly weather forecast for a specific location
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.weather.forecast.hourly(latitude=47.6061, longitude=-122.3328, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**latitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[Timezone]` 
    
</dd>
</dl>

<dl>
<dd>

**units:** `typing.Optional[Units]` 
    
</dd>
</dl>

<dl>
<dd>

**include_past:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Weather Experimental
<details><summary><code>client.weather.experimental.<a href="src/silurian/weather/experimental/client.py">extended</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get hourly weather forecast for a specific location and time
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.weather.experimental.extended(latitude=47.6061, longitude=-122.3328, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**latitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[Timezone]` 
    
</dd>
</dl>

<dl>
<dd>

**units:** `typing.Optional[Units]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Weather Experimental Regional
<details><summary><code>client.weather.experimental.regional.<a href="src/silurian/weather/experimental/regional/client.py">usa</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get hourly weather forecast for a specific location and time
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.weather.experimental.regional.usa(latitude=47.6061, longitude=-122.3328, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**latitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[Timezone]` 
    
</dd>
</dl>

<dl>
<dd>

**units:** `typing.Optional[Units]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Weather Experimental Personalized
<details><summary><code>client.weather.experimental.personalized.<a href="src/silurian/weather/experimental/personalized/client.py">total_energies</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return asset‑level forecast data as a JSON ForecastTable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
client = Earth(api_key="YOUR_API_KEY", )
client.weather.experimental.personalized.total_energies()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Weather Past Forecast
<details><summary><code>client.weather.past.forecast.<a href="src/silurian/weather/past/forecast/client.py">daily</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get daily weather forecast for a specific location and time
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
import datetime
client = Earth(api_key="YOUR_API_KEY", )
client.weather.past.forecast.daily(latitude=47.6061, longitude=-122.3328, time=datetime.datetime.fromisoformat("2024-01-01 00:00:00+00:00", ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**latitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**time:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[Timezone]` 
    
</dd>
</dl>

<dl>
<dd>

**units:** `typing.Optional[Units]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.weather.past.forecast.<a href="src/silurian/weather/past/forecast/client.py">hourly</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get hourly weather forecast for a specific location and time
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
import datetime
client = Earth(api_key="YOUR_API_KEY", )
client.weather.past.forecast.hourly(latitude=47.6061, longitude=-122.3328, time=datetime.datetime.fromisoformat("2024-01-01 00:00:00+00:00", ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**latitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**time:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[Timezone]` 
    
</dd>
</dl>

<dl>
<dd>

**units:** `typing.Optional[Units]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

