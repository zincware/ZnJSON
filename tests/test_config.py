import pytest

import znjson.converter
from znjson import ConverterBase, exceptions


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    """Fixture to execute before and after a test is run"""
    znjson.config.deregister(znjson.config.ACTIVE_CONVERTER)
    yield  # this is where the testing happens
    znjson.config.register()


class NumberConverterA(ConverterBase):
    instance = int
    representation = "int"
    level = 100

    def encode(self, obj: int) -> str:
        return str(obj)

    def decode(self, value: str) -> int:
        return int(value)


class NumberConverterB(NumberConverterA):
    """Different converter to A with the same representation string"""

    pass


@pytest.mark.parametrize(
    "converters",
    (
        [],
        [znjson.converter.PathlibConverter],
        [znjson.converter.PathlibConverter, znjson.converter.PathlibConverter],
        [znjson.converter.PathlibConverter, znjson.converter.ClassConverter],
    ),
)
def test_register(converters):
    znjson.config.register(converters)
    assert set(znjson.config.ACTIVE_CONVERTER) == set(converters)


def test_register_PathlibConverter():
    znjson.config.register(znjson.converter.PathlibConverter)
    assert znjson.config.ACTIVE_CONVERTER == [znjson.converter.PathlibConverter]


def test_deregister_single():
    znjson.config.register(
        [znjson.converter.PathlibConverter, znjson.converter.ClassConverter]
    )

    znjson.config.deregister(znjson.converter.PathlibConverter)

    assert znjson.config.ACTIVE_CONVERTER == [znjson.converter.ClassConverter]


def test_deregister_multiple():
    znjson.config.register(
        [znjson.converter.PathlibConverter, znjson.converter.ClassConverter]
    )

    znjson.config.deregister(
        [znjson.converter.PathlibConverter, znjson.converter.ClassConverter]
    )

    assert znjson.config.ACTIVE_CONVERTER == []


def test_register_non_unique():
    with pytest.raises(exceptions.NonUniqueRepresentation):
        znjson.config.register([NumberConverterA, NumberConverterB])
