"""Use base64 encoding to ASCII for large numpy arrays"""
import base64
import io

import numpy as np

from znjson import ConverterBase


class NumpyConverter(ConverterBase):
    instance = np.ndarray
    representation = "np.ndarray64"
    level = 30

    def encode(self, obj):
        with io.BytesIO() as f:
            np.save(f, obj)
            f.seek(0)
            return base64.b64encode(f.read()).decode("ascii")

    def decode(self, value):
        with io.BytesIO() as f:
            f.write(base64.b64decode(value))
            f.seek(0)
            return np.load(f)
