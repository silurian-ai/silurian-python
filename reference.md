# Reference
## Portfolios
<details><summary><code>client.portfolios.<a href="src/silurian/portfolios/client.py">features</a>(...) -> FeatureCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a GeoJSON FeatureCollection of features for a portfolio.
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
from silurian.environment import EarthEnvironment

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.portfolios.features(
    portfolio_id="portfolio_id",
    x=1,
    y=1,
    z=1,
    country="country",
)

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

**portfolio_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**x:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**y:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**z:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` 
    
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

<details><summary><code>client.portfolios.<a href="src/silurian/portfolios/client.py">forecasts</a>(...) -> TimeSeriesFeatureCollectionModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a GeoJSON FeatureCollection of forecasts for a portfolio.
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
from silurian.environment import EarthEnvironment
import datetime

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.portfolios.forecasts(
    portfolio_id="portfolio_id",
    id=[
        "id"
    ],
    variables=[
        "variables"
    ],
    init_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

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

**portfolio_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**init_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

<details><summary><code>client.portfolios.<a href="src/silurian/portfolios/client.py">observations</a>(...) -> TimeSeriesFeatureCollectionModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a GeoJSON FeatureCollection of observations for a portfolio.
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
from silurian.environment import EarthEnvironment
import datetime

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.portfolios.observations(
    portfolio_id="portfolio_id",
    id=[
        "id"
    ],
    variables=[
        "variables"
    ],
    valid_time_start=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    valid_time_end=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

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

**portfolio_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**valid_time_start:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**valid_time_end:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

<details><summary><code>client.portfolios.<a href="src/silurian/portfolios/client.py">init_time</a>(...) -> datetime.datetime</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the latest initialization time for a portfolio.
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
from silurian.environment import EarthEnvironment
import datetime

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.portfolios.init_time(
    portfolio_id="portfolio_id",
    time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

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

**portfolio_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**time:** `datetime.datetime` 
    
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
<details><summary><code>client.cyclones.forecasts.<a href="src/silurian/cyclones/forecasts/client.py">list</a>(...) -> typing.List[CycloneForecastResponse]</code></summary>
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
from silurian.environment import EarthEnvironment
import datetime

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.cyclones.forecasts.list(
    time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    min_storm_category=1,
    basin_ids=[
        "basin_ids"
    ],
    model="OFCL",
)

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

**time:** `typing.Optional[datetime.datetime]` — *Default value: (current time) - Default time zone: UTC*
    
</dd>
</dl>

<dl>
<dd>

**min_storm_category:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**basin_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

<details><summary><code>client.cyclones.forecasts.<a href="src/silurian/cyclones/forecasts/client.py">track</a>(...) -> FeatureCollection</code></summary>
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
from silurian.environment import EarthEnvironment
import datetime

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.cyclones.forecasts.track(
    storm_id="storm_id",
    time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    max_lead_time="max_lead_time",
    model="OFCL",
)

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

**time:** `typing.Optional[datetime.datetime]` — *Default value: (current time) - Default time zone: UTC*
    
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

<details><summary><code>client.cyclones.forecasts.<a href="src/silurian/cyclones/forecasts/client.py">cone</a>(...) -> FeatureCollection</code></summary>
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
from silurian.environment import EarthEnvironment
import datetime

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.cyclones.forecasts.cone(
    storm_id="storm_id",
    time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    max_lead_time="max_lead_time",
    smooth_cone=True,
    model="OFCL",
)

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

**time:** `typing.Optional[datetime.datetime]` — *Default value: (current time) - Default time zone: UTC*
    
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
<details><summary><code>client.weather.forecast.<a href="src/silurian/weather/forecast/client.py">daily</a>(...) -> DailyWeatherResponse</code></summary>
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
from silurian.environment import EarthEnvironment

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.weather.forecast.daily(
    latitude=47.6061,
    longitude=-122.3328,
    timezone="local",
    units="metric",
)

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

**timezone:** `typing.Optional[typing.Literal]` 
    
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

<details><summary><code>client.weather.forecast.<a href="src/silurian/weather/forecast/client.py">hourly</a>(...) -> HourlyWeatherResponse</code></summary>
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
from silurian.environment import EarthEnvironment

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.weather.forecast.hourly(
    latitude=47.6061,
    longitude=-122.3328,
    timezone="local",
    units="metric",
    include_past=True,
)

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
<details><summary><code>client.weather.experimental.<a href="src/silurian/weather/experimental/client.py">extended</a>(...) -> HourlyWeatherResponse</code></summary>
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
from silurian.environment import EarthEnvironment

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.weather.experimental.extended(
    latitude=47.6061,
    longitude=-122.3328,
    timezone="local",
    units="metric",
)

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
<details><summary><code>client.weather.experimental.regional.<a href="src/silurian/weather/experimental/regional/client.py">usa</a>(...) -> GftusHourlyWeatherResponse</code></summary>
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
from silurian.environment import EarthEnvironment

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.weather.experimental.regional.usa(
    latitude=47.6061,
    longitude=-122.3328,
    timezone="local",
    units="metric",
)

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from silurian import Earth
from silurian.environment import EarthEnvironment

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

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

## Weather Experimental Past Regional
<details><summary><code>client.weather.experimental.past.regional.<a href="src/silurian/weather/experimental/past/regional/client.py">usa</a>(...) -> GftusHourlyWeatherResponse</code></summary>
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
from silurian.environment import EarthEnvironment
import datetime

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.weather.experimental.past.regional.usa(
    latitude=47.6061,
    longitude=-122.3328,
    time=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    timezone="local",
    units="metric",
)

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

**time:** `datetime.datetime` 
    
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

## Weather Past Forecast
<details><summary><code>client.weather.past.forecast.<a href="src/silurian/weather/past/forecast/client.py">daily</a>(...) -> DailyWeatherResponse</code></summary>
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
from silurian.environment import EarthEnvironment
import datetime

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.weather.past.forecast.daily(
    latitude=47.6061,
    longitude=-122.3328,
    time=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    timezone="local",
    units="metric",
)

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

**time:** `datetime.datetime` 
    
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

<details><summary><code>client.weather.past.forecast.<a href="src/silurian/weather/past/forecast/client.py">hourly</a>(...) -> HourlyWeatherResponse</code></summary>
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
from silurian.environment import EarthEnvironment
import datetime

client = Earth(
    api_key="<value>",
    environment=EarthEnvironment.PRODUCTION,
)

client.weather.past.forecast.hourly(
    latitude=47.6061,
    longitude=-122.3328,
    time=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    timezone="local",
    units="metric",
)

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

**time:** `datetime.datetime` 
    
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

