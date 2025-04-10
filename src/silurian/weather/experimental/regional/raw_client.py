# This file was auto-generated by Fern from our API Definition.

from ....core.client_wrapper import SyncClientWrapper
import typing
from ....types.timezone import Timezone
from ....types.units import Units
from ....core.request_options import RequestOptions
from ....core.http_response import HttpResponse
from ....types.gftus_hourly_weather_response import GftusHourlyWeatherResponse
from ....core.pydantic_utilities import parse_obj_as
from ....errors.unprocessable_entity_error import UnprocessableEntityError
from ....types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ....core.api_error import ApiError
from ....core.client_wrapper import AsyncClientWrapper
from ....core.http_response import AsyncHttpResponse


class RawRegionalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def usa(
        self,
        *,
        latitude: float,
        longitude: float,
        timezone: typing.Optional[Timezone] = None,
        units: typing.Optional[Units] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GftusHourlyWeatherResponse]:
        """
        Get hourly weather forecast for a specific location and time

        Parameters
        ----------
        latitude : float

        longitude : float

        timezone : typing.Optional[Timezone]

        units : typing.Optional[Units]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GftusHourlyWeatherResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/regional/usa",
            method="GET",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "timezone": timezone,
                "units": units,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GftusHourlyWeatherResponse,
                    parse_obj_as(
                        type_=GftusHourlyWeatherResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawRegionalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def usa(
        self,
        *,
        latitude: float,
        longitude: float,
        timezone: typing.Optional[Timezone] = None,
        units: typing.Optional[Units] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GftusHourlyWeatherResponse]:
        """
        Get hourly weather forecast for a specific location and time

        Parameters
        ----------
        latitude : float

        longitude : float

        timezone : typing.Optional[Timezone]

        units : typing.Optional[Units]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GftusHourlyWeatherResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/regional/usa",
            method="GET",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "timezone": timezone,
                "units": units,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GftusHourlyWeatherResponse,
                    parse_obj_as(
                        type_=GftusHourlyWeatherResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
