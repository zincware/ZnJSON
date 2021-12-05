import pytest
import json
import pathlib


@pytest.fixture
def my_path():
    return pathlib.Path("/test/path/file.txt")


def test_encode(my_path):
    import znconv

    znconv.register(znconv.converter.PathlibConverter)
    _ = json.dumps(my_path, cls=znconv.ZnEncoder)
    # raise NotImplementedError(json.dumps(my_path, cls=znconv.ZnEncoder))


def test_decode(my_path):
    import znconv

    # znconv.register(znconv.converter.PathlibConverter)
    encoded_str = json.dumps(my_path, cls=znconv.ZnEncoder)
    assert json.loads(encoded_str, cls=znconv.ZnDecoder) == my_path
