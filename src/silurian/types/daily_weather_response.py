# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .daily_weather_response_units import DailyWeatherResponseUnits
from .daily_conditions import DailyConditions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DailyWeatherResponse(UniversalBaseModel):
    latitude: float
    longitude: float
    timezone: str
    utc_offset: int
    elevation: typing.Optional[int] = None
    units: DailyWeatherResponseUnits
    daily: typing.List[DailyConditions]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
