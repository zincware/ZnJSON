import json

import numpy as np
import pytest

import znjson

znjson.register(znjson.converter.ClassConverter)


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
