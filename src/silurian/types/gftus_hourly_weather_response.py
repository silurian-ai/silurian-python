# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import datetime as dt
import typing
from .gftus_base_units import GftusBaseUnits
from .gftus_hourly_conditions import GftusHourlyConditions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GftusHourlyWeatherResponse(UniversalBaseModel):
    latitude: float
    longitude: float
    forecast_time: dt.datetime
    timezone: str
    utc_offset: int
    elevation: typing.Optional[int] = None
    units: GftusBaseUnits
    hourly: typing.List[GftusHourlyConditions]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
