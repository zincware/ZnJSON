import json
import pathlib

import pytest

import znjson


@pytest.fixture
def simple_dict():
    return {"a": 10, "b": 20}


@pytest.fixture()
def pathlib_path():
    return pathlib.Path("test_path.txt")


@pytest.fixture()
def serialized_pathlib_path():
    return '{"_type": "pathlib.Path", "value": "test_path.txt"}'


def test_encoder_serializable(simple_dict):
    _ = json.dumps(simple_dict, cls=znjson.ZnEncoder)


def test_decoder_serializable(simple_dict):
    data_str = json.dumps(simple_dict, cls=znjson.ZnEncoder)

    assert simple_dict == json.loads(data_str, cls=znjson.ZnDecoder)
