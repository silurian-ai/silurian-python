# Reference
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

client = Earth(
    api_key="YOUR_API_KEY",
)
client.weather.forecast.daily(
    latitude=47.6061,
    longitude=-122.3328,
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

client = Earth(
    api_key="YOUR_API_KEY",
)
client.weather.forecast.hourly(
    latitude=47.6061,
    longitude=-122.3328,
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

