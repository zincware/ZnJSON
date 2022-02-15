import json

import numpy as np
import pytest

import znjson

znjson.register([znjson.converter.NumpyConverter, znjson.converter.SmallNumpyConverter])


@pytest.fixture
def numpy_array():
    return np.arange(100)


def test_encode(numpy_array):
    arr = json.dumps(numpy_array, cls=znjson.ZnEncoder)
    # check that the correct encoder is used
    assert arr.startswith('{"_type": "np.ndarray64"')


def test_decode(numpy_array):
    encoded_str = json.dumps(numpy_array, cls=znjson.ZnEncoder)
    np.testing.assert_array_equal(
        numpy_array, json.loads(encoded_str, cls=znjson.ZnDecoder)
    )
