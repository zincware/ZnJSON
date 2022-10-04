import json
from datetime import datetime

import znjson
from znjson import ConverterBase


class DatetimeConverter(ConverterBase):
    """Encode/Decode datetime objects

    Attributes
    ----------
    level: int
        Priority of this converter over others.
        A higher level will be used first, if there
        are multiple converters available
    representation: str
        An unique identifier for this converter.
    instance:
        Used to select the correct converter.
        This should fulfill isinstance(other, self.instance)
        or __eq__ should be overwritten.
    """

    level = 100
    representation = "datetime"
    instance = datetime

    def _encode(self, obj: datetime) -> str:
        """Convert the datetime object to str / isoformat"""
        return obj.isoformat()

    def _decode(self, value: str) -> datetime:
        """Create datetime object from str / isoformat"""
        return datetime.fromisoformat(value)


def test__encode():
    znjson.config.register(DatetimeConverter)
    date = datetime.fromisoformat("2022-10-03")
    assert date == json.loads(
        json.dumps(date, cls=znjson.ZnEncoder), cls=znjson.ZnDecoder
    )
    znjson.config.deregister(DatetimeConverter)


def test_old_register():
    znjson.register(DatetimeConverter)
    date = datetime.fromisoformat("2022-10-03")
    assert date == json.loads(
        json.dumps(date, cls=znjson.ZnEncoder), cls=znjson.ZnDecoder
    )
    znjson.deregister(DatetimeConverter)
