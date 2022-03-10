import json

import numpy as np
import pytest

import znjson


@pytest.fixture
def numpy_array():
    return np.arange(10)


@pytest.fixture
def numpy_array_large():
    return np.arange(1000)


@pytest.fixture
def numpy_float_array():
    return np.arange(10).astype(float)


def test_encode(numpy_array):
    arr = json.dumps(numpy_array, cls=znjson.ZnEncoder)
    assert arr == '{"_type": "np.ndarray_small", "value": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}'


def test_encode_large(numpy_array_large):
    arr = json.dumps(numpy_array_large, cls=znjson.ZnEncoder)
    assert arr.startswith('{"_type": "np.ndarray64"')


def test_encode_float(numpy_float_array):
    arr = json.dumps(numpy_float_array, cls=znjson.ZnEncoder)
    assert (
        arr
        == '{"_type": "np.ndarray_small", "value": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0,'
        " 7.0, 8.0, 9.0]}"
    )


def test_decode(numpy_array):
    arr = '{"_type": "np.ndarray_small", "value": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}'

    np.testing.assert_array_equal(numpy_array, json.loads(arr, cls=znjson.ZnDecoder))


def test_decode_float(numpy_float_array):
    arr = (
        '{"_type": "np.ndarray_small", "value": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0,'
        " 8.0, 9.0]}"
    )

    np.testing.assert_array_equal(
        numpy_float_array, json.loads(arr, cls=znjson.ZnDecoder)
    )
