import datetime as dt

from freezegun import freeze_time

from silurian.core.datetime_utils import serialize_datetime


class TestDatetimeUtils:
    def test_serialize_datetime_with_utc_timezone(self):
        # Test that UTC timezone datetimes are serialized with 'Z'
        datetime_utc = dt.datetime(2023, 1, 15, 12, 30, 45, tzinfo=dt.timezone.utc)
        result = serialize_datetime(datetime_utc)
        assert result == "2023-01-15T12:30:45Z"

    def test_serialize_datetime_with_non_utc_timezone(self):
        # Test that non-UTC timezone datetimes are serialized with offset
        timezone_offset = dt.timezone(dt.timedelta(hours=5, minutes=30))  # +05:30
        datetime_non_utc = dt.datetime(2023, 1, 15, 12, 30, 45, tzinfo=timezone_offset)
        result = serialize_datetime(datetime_non_utc)
        assert result == "2023-01-15T12:30:45+05:30"

    def test_serialize_datetime_without_timezone(self):
        # Test that datetimes without timezone are serialized as is (without adding local timezone)
        naive_datetime = dt.datetime(2023, 1, 15, 12, 30, 45)
        result = serialize_datetime(naive_datetime)
        assert result == "2023-01-15T12:30:45"

    @freeze_time("2023-01-15 12:30:45")
    def test_serialize_datetime_without_timezone_frozen_time(self):
        # Test using freeze_time to ensure consistent behavior regardless of execution timezone
        naive_datetime = dt.datetime(2023, 1, 15, 12, 30, 45)
        result = serialize_datetime(naive_datetime)
        assert result == "2023-01-15T12:30:45"

    @freeze_time("2023-01-15 12:30:45", tz_offset=5)  # UTC+5
    def test_serialize_datetime_with_frozen_timezone(self):
        # Test with freeze_time setting a specific timezone offset
        naive_datetime = dt.datetime(2023, 1, 15, 12, 30, 45)
        result = serialize_datetime(naive_datetime)
        # Should still return the naive datetime string because the code no longer applies local timezone
        assert result == "2023-01-15T12:30:45"

    def test_serialize_datetime_with_microseconds(self):
        # Test that microseconds are preserved in the serialization
        datetime_with_micros = dt.datetime(
            2023, 1, 15, 12, 30, 45, 123456, tzinfo=dt.timezone.utc
        )
        result = serialize_datetime(datetime_with_micros)
        assert result == "2023-01-15T12:30:45.123456Z"

