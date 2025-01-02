# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import datetime as dt
import typing
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class HourlyConditions(UniversalBaseModel):
    timestamp: dt.datetime
    temperature: typing.Optional[float] = None
    dewpoint_temperature: typing.Optional[float] = None
    precipitation_accumulation: typing.Optional[float] = None
    wind_speed: typing.Optional[float] = None
    wind_direction: typing.Optional[float] = None
    pressure: typing.Optional[float] = None
    downward_solar_radiation: typing.Optional[float] = None
    wind_speed_100_m: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="wind_speed_100m")] = None
    wind_direction_100_m: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="wind_direction_100m")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
