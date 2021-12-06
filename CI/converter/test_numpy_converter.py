import numpy as np
import pytest
import json

import znjson

znjson.register(znjson.converter.NumpyConverter)


@pytest.fixture
def numpy_array():
    return np.arange(10)


def test_encode(numpy_array):
    _ = json.dumps(numpy_array, cls=znjson.ZnEncoder)


def test_decode(numpy_array):
    encoded_str = json.dumps(numpy_array, cls=znjson.ZnEncoder)
    np.testing.assert_array_equal(
        numpy_array, json.loads(encoded_str, cls=znjson.ZnDecoder)
    )
