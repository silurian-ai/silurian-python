# Reference
## Forecasts
<details><summary><code>client.forecasts.<a href="src/silurian/forecasts/client.py">create_daily</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get daily weather forecast for a specific location
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
from silurian import Silurian

client = Silurian(
    api_key="YOUR_API_KEY",
)
client.forecasts.create_daily(
    latitude=1.1,
    longitude=1.1,
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

<details><summary><code>client.forecasts.<a href="src/silurian/forecasts/client.py">create_hourly</a>(...)</code></summary>
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
from silurian import Silurian

client = Silurian(
    api_key="YOUR_API_KEY",
)
client.forecasts.create_hourly(
    latitude=1.1,
    longitude=1.1,
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

