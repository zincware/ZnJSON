import json

import pytest

import znjson


class HelloWorld:
    def __init__(self):
        self.name = "HelloWorld"


@pytest.fixture
def example_class():
    return HelloWorld()


def test_encode(example_class):
    _ = json.dumps(example_class, cls=znjson.ZnEncoder)


def test_decode(example_class):
    encoded_str = json.dumps(example_class, cls=znjson.ZnEncoder)
    assert isinstance(json.loads(encoded_str, cls=znjson.ZnDecoder), type(example_class))


def test_unable_to_encode():
    class OutOfScope:
        """Can not be imported, so it can not be encoded"""

        pass

    with pytest.raises(TypeError):
        json.dumps(OutOfScope(), cls=znjson.ZnEncoder)
