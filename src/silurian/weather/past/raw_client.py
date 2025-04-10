# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
from ...core.client_wrapper import AsyncClientWrapper


class RawPastClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper


class AsyncRawPastClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
