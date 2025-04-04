# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
from .forecast.client import ForecastClient
from .experimental.client import ExperimentalClient
from .past.client import PastClient
from ..core.client_wrapper import AsyncClientWrapper
from .forecast.client import AsyncForecastClient
from .experimental.client import AsyncExperimentalClient
from .past.client import AsyncPastClient


class WeatherClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.forecast = ForecastClient(client_wrapper=self._client_wrapper)
        self.experimental = ExperimentalClient(client_wrapper=self._client_wrapper)
        self.past = PastClient(client_wrapper=self._client_wrapper)


class AsyncWeatherClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.forecast = AsyncForecastClient(client_wrapper=self._client_wrapper)
        self.experimental = AsyncExperimentalClient(client_wrapper=self._client_wrapper)
        self.past = AsyncPastClient(client_wrapper=self._client_wrapper)
