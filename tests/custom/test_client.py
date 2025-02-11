import os
from datetime import datetime

import pytest

from silurian import AsyncEarth, Earth

API_KEY_ENV = "SILURIAN_EARTH_API_KEY"
SEATTLE_COORDS = {"latitude": 47.6061, "longitude": -122.3328}
PAST_ARGS = {**SEATTLE_COORDS, "time": datetime.fromisoformat("2025-02-01T00:00:00")}


skip_if_no_api = pytest.mark.skipif(
    not os.getenv(API_KEY_ENV),
    reason=f"Skipping live API tests. {API_KEY_ENV} environment variable not set",
)


@skip_if_no_api
def test_sync_client() -> None:
    client = Earth(api_key=os.environ[API_KEY_ENV])
    assert isinstance(client, Earth)

    # Test forecast endpoints
    assert client.weather.forecast.daily(**SEATTLE_COORDS) is not None
    assert client.weather.forecast.hourly(**SEATTLE_COORDS) is not None

    # Test past weather endpoints
    assert client.weather.past.forecast.daily(**PAST_ARGS) is not None
    assert client.weather.past.forecast.hourly(**PAST_ARGS) is not None


@skip_if_no_api
@pytest.mark.asyncio
class TestAsyncWeatherEndpoints:
    @pytest.fixture
    async def client(self):
        return AsyncEarth(api_key=os.environ[API_KEY_ENV])

    async def test_forecast_daily(self, client) -> None:
        response = await client.weather.forecast.daily(**SEATTLE_COORDS)
        assert response is not None

    async def test_forecast_hourly(self, client) -> None:
        response = await client.weather.forecast.hourly(**SEATTLE_COORDS)
        assert response is not None

    async def test_past_daily(self, client) -> None:
        response = await client.weather.past.forecast.daily(**PAST_ARGS)
        assert response is not None

    async def test_past_hourly(self, client) -> None:
        response = await client.weather.past.forecast.hourly(**PAST_ARGS)
        assert response is not None
