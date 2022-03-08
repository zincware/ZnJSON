import pytest

import znjson.converter


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    """Fixture to execute before and after a test is run"""
    znjson.deregister(znjson.config.ACTIVE_CONVERTER)
    yield  # this is where the testing happens
    znjson.register()


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
    znjson.register(converters)
    assert set(znjson.config.ACTIVE_CONVERTER) == set(converters)


def test_register_PathlibConverter():
    znjson.register(znjson.converter.PathlibConverter)
    assert znjson.config.ACTIVE_CONVERTER == [znjson.converter.PathlibConverter]


def test_deregister_single():
    znjson.register([znjson.converter.PathlibConverter, znjson.converter.ClassConverter])

    znjson.deregister(znjson.converter.PathlibConverter)

    assert znjson.config.ACTIVE_CONVERTER == [znjson.converter.ClassConverter]


def test_deregister_multiple():
    znjson.register([znjson.converter.PathlibConverter, znjson.converter.ClassConverter])

    znjson.deregister(
        [znjson.converter.PathlibConverter, znjson.converter.ClassConverter]
    )

    assert znjson.config.ACTIVE_CONVERTER == []
