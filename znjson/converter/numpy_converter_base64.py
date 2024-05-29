"""Use base64 encoding to ASCII for large numpy arrays"""

import functools

import numpy as np

from znjson.base import ConverterBase


class NumpyConverter(ConverterBase):
    """Use base64 encoding to ASCII for large numpy arrays"""

    instance = np.ndarray
    representation = "np.ndarray_b64"
    level = 30

    def encode(self, obj):
        """Encode the numpy array"""
        return self.save_to_b64(method=functools.partial(np.save, arr=obj))

    def decode(self, value):
        """Decode the numpy array"""
        return self.load_from_b64(value, method=np.load)
