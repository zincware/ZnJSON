import json
import pathlib

import pytest


@pytest.fixture
def my_path():
    return pathlib.Path("/test/path/file.txt")


def test_encode(my_path):
    import znjson

    znjson.register(znjson.converter.PathlibConverter)
    _ = json.dumps(my_path, cls=znjson.ZnEncoder)
    # raise NotImplementedError(json.dumps(my_path, cls=znconv.ZnEncoder))


def test_decode(my_path):
    import znjson

    # znconv.register(znconv.converter.PathlibConverter)
    encoded_str = json.dumps(my_path, cls=znjson.ZnEncoder)
    assert json.loads(encoded_str, cls=znjson.ZnDecoder) == my_path
