import json

import numpy as np
import pytest

import znjson.converter


@pytest.fixture
def numpy_array():
    return np.arange(100)


def test_encode(numpy_array):
    encoded_str = json.dumps(numpy_array, cls=znjson.ZnEncoder)
    # check that the correct encoder is used
    assert encoded_str.startswith('{"_type": "np.ndarray_b64"')


def test_encode_direct(numpy_array):
    encoded_str = znjson.dumps(numpy_array, converter=znjson.converter.NumpyConverter)
    assert encoded_str.startswith('{"_type": "np.ndarray_b64"')
    encoded_str = znjson.dumps(numpy_array, cls=znjson.ZnEncoder.from_converters([znjson.converter.NumpyConverter]))
    assert encoded_str.startswith('{"_type": "np.ndarray_b64"')

    with pytest.raises(TypeError):
        _ = znjson.dumps(numpy_array, converter=znjson.converter.NumpyConverter, cls=znjson.ZnEncoder)

def test_decode(numpy_array):
    encoded_str = json.dumps(numpy_array, cls=znjson.ZnEncoder)
    np.testing.assert_array_equal(
        numpy_array, json.loads(encoded_str, cls=znjson.ZnDecoder)
    )


def test_decode_direct(numpy_array):
    encoded_str = znjson.dumps(numpy_array, converter=znjson.converter.NumpyConverter)
    np.testing.assert_array_equal(
        numpy_array,
        znjson.loads(encoded_str, converter=znjson.converter.NumpyConverter),
    )
    np.testing.assert_array_equal(
        numpy_array,
        znjson.loads(encoded_str, cls=znjson.ZnDecoder.from_converters([znjson.converter.NumpyConverter])),
    )
    with pytest.raises(TypeError):
        _ = znjson.loads(encoded_str, converter=znjson.converter.NumpyConverter, cls=znjson.ZnDecoder)


def test_decode_missing_converter(numpy_array):
    with pytest.raises(TypeError):
        _ = znjson.dumps(numpy_array, converter=[])
