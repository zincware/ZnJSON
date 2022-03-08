import json

import numpy as np
import pytest

import znjson


@pytest.fixture
def numpy_array():
    return np.arange(100)


def test_encode(numpy_array):
    encoded_str = json.dumps(numpy_array, cls=znjson.ZnEncoder)
    # check that the correct encoder is used
    assert encoded_str.startswith('{"_type": "np.ndarray64"')


def test_decode(numpy_array):
    encoded_str = json.dumps(numpy_array, cls=znjson.ZnEncoder)
    np.testing.assert_array_equal(
        numpy_array, json.loads(encoded_str, cls=znjson.ZnDecoder)
    )


def test_decode_latin1(numpy_array):
    znjson.deregister(znjson.converter.NumpyConverter)
    encoded_str = json.dumps(numpy_array, cls=znjson.ZnEncoder)
    # check that the correct encoder is used
    assert encoded_str.startswith('{"_type": "np.ndarray"')
    znjson.register(znjson.converter.NumpyConverter)
    np.testing.assert_array_equal(
        numpy_array, json.loads(encoded_str, cls=znjson.ZnDecoder)
    )
