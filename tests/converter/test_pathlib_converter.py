import json
import pathlib

import pytest


@pytest.fixture
def my_path():
    return pathlib.Path("/test/path/file.txt")


@pytest.fixture()
def path_list():
    return [pathlib.Path(f"{x}.json") for x in range(3)]


def test_encode(my_path):
    import znjson

    znjson.config.register(znjson.converter.PathlibConverter)
    _ = json.dumps(my_path, cls=znjson.ZnEncoder)
    # raise NotImplementedError(json.dumps(my_path, cls=znconv.ZnEncoder))


def test_decode(my_path):
    import znjson

    # znconv.register(znconv.converter.PathlibConverter)
    encoded_str = json.dumps(my_path, cls=znjson.ZnEncoder)
    assert json.loads(encoded_str, cls=znjson.ZnDecoder) == my_path


def test_encode_lst(path_list):
    import znjson

    znjson.config.register(znjson.converter.PathlibConverter)
    _ = json.dumps(path_list, cls=znjson.ZnEncoder)


def test_decode_lst(path_list):
    import znjson

    # znconv.register(znconv.converter.PathlibConverter)
    encoded_str = json.dumps(path_list, cls=znjson.ZnEncoder)
    assert json.loads(encoded_str, cls=znjson.ZnDecoder) == path_list
