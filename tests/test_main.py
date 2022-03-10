import json
import pathlib

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
    function = lambda x: x

    with pytest.raises(TypeError):
        json.dumps(function, cls=znjson.ZnEncoder)


def test_not_decodeable():
    data_str = '{"_type": "unknown", "value": ""}'

    with pytest.raises(TypeError):
        json.loads(data_str, cls=znjson.ZnDecoder)