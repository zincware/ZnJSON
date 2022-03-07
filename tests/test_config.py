import pytest

import znjson.converter


@pytest.fixture()
def deregister_all():
    znjson.deregister(znjson.config.ACTIVE_CONVERTER)


def test_empty_converter(deregister_all):
    assert znjson.config.ACTIVE_CONVERTER == []


def test_register_PathlibConverter(deregister_all):
    znjson.register(znjson.converter.PathlibConverter)
    assert znjson.config.ACTIVE_CONVERTER == [znjson.converter.PathlibConverter]


def test_register_PathlibConverter_twice(deregister_all):
    znjson.register(
        [znjson.converter.PathlibConverter, znjson.converter.PathlibConverter]
    )
    assert znjson.config.ACTIVE_CONVERTER == [znjson.converter.PathlibConverter]


def test_register_PathlibConverter_ClassConverter(deregister_all):
    znjson.register([znjson.converter.PathlibConverter, znjson.converter.ClassConverter])
    assert znjson.config.ACTIVE_CONVERTER == [
        znjson.converter.ClassConverter,
        znjson.converter.PathlibConverter,
    ]


def test_deregister_single(deregister_all):
    znjson.register([znjson.converter.PathlibConverter, znjson.converter.ClassConverter])

    znjson.deregister(znjson.converter.PathlibConverter)

    assert znjson.config.ACTIVE_CONVERTER == [znjson.converter.ClassConverter]


def test_deregister_multiple(deregister_all):
    znjson.register([znjson.converter.PathlibConverter, znjson.converter.ClassConverter])

    znjson.deregister(
        [znjson.converter.PathlibConverter, znjson.converter.ClassConverter]
    )

    assert znjson.config.ACTIVE_CONVERTER == []
