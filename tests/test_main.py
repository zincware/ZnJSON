import json
import pathlib

import numpy as np
import pytest

import znjson


@pytest.fixture
def simple_dict():
    return {"a": 10, "b": 20}


def test_encoder_serializable(simple_dict):
    _ = json.dumps(simple_dict, cls=znjson.ZnEncoder)


def test_decoder_serializable(simple_dict):
    data_str = json.dumps(simple_dict, cls=znjson.ZnEncoder)

    assert simple_dict == json.loads(data_str, cls=znjson.ZnDecoder)


def test_decode_pathlib():
    data_str = '{"_type": "pathlib.Path", "value": "test_path.txt"}'

    assert json.loads(data_str, cls=znjson.ZnDecoder) == pathlib.Path("test_path.txt")


def test_decode_pathlib_wo__type():
    data_str = '{"value": "test_path.txt"}'

    assert json.loads(data_str, cls=znjson.ZnDecoder) == {"value": "test_path.txt"}


def test_decode_pathlib_wo_value():
    data_str = '{"_type": "pathlib.Path"}'

    assert json.loads(data_str, cls=znjson.ZnDecoder) == {"_type": "pathlib.Path"}


def test_not_encodeable():
    def function():
        ...

    with pytest.raises(TypeError):
        json.dumps(function, cls=znjson.ZnEncoder)


def test_not_decodeable():
    data_str = '{"_type": "unknown", "value": ""}'

    with pytest.raises(TypeError):
        json.loads(data_str, cls=znjson.ZnDecoder)


@pytest.mark.parametrize("enable", (True, False))
def test_from_converter(enable):
    data = np.arange(10)

    if enable:
        encoded_str = json.dumps(
            data,
            cls=znjson.ZnEncoder.from_converters([znjson.converter.NumpyConverterSmall]),
        )
        assert json.loads(encoded_str)["_type"] == "np.ndarray_small"
    else:
        with pytest.raises(TypeError):
            # only can encode pathlib
            _ = json.dumps(
                data,
                cls=znjson.ZnEncoder.from_converters([znjson.converter.PathlibConverter]),
            )


def test_from_converter_multi():
    """Check that it does not mess with any global configurations"""
    array = np.arange(10)
    path = pathlib.Path.cwd()

    with pytest.raises(TypeError):
        _ = json.dumps({array, path}, cls=znjson.ZnEncoder.from_converters([]))

    encoded_str = json.dumps(
        array, cls=znjson.ZnEncoder.from_converters(znjson.converter.NumpyConverter)
    )
    assert json.loads(encoded_str)["_type"] == "np.ndarray_b64"

    encoded_str = json.dumps(
        [array, path],
        cls=znjson.ZnEncoder.from_converters(
            [znjson.converter.NumpyConverter, znjson.converter.PathlibConverter]
        ),
    )
    assert json.loads(encoded_str)[0]["_type"] == "np.ndarray_b64"
    assert json.loads(encoded_str)[1]["_type"] == "pathlib.Path"

    with pytest.raises(TypeError):
        _ = json.dumps({array, path}, cls=znjson.ZnEncoder.from_converters([]))

    encoded_str = json.dumps(
        [array, path], cls=znjson.ZnEncoder.from_converters([], add_default=True)
    )
    assert json.loads(encoded_str)[0]["_type"] == "np.ndarray_small"
    assert json.loads(encoded_str)[1]["_type"] == "pathlib.Path"
