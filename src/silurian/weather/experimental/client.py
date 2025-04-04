# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
from .regional.client import RegionalClient
from ...core.client_wrapper import AsyncClientWrapper
from .regional.client import AsyncRegionalClient


class ExperimentalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.regional = RegionalClient(client_wrapper=self._client_wrapper)


class AsyncExperimentalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.regional = AsyncRegionalClient(client_wrapper=self._client_wrapper)
