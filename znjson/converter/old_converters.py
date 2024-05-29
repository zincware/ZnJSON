"""Converters that should not be used anymore but are
still available for backwards compatibility."""

import io

import numpy as np

from znjson.converter.numpy_converter_base64 import NumpyConverter


class NumpyConverterLatin1(NumpyConverter):
    """Old numpy converter"""

    representation = "np.ndarray"
    level = 1

    def encode(self, obj):
        with io.BytesIO() as file:
            np.save(file, obj)
            file.seek(0)
            return file.read().decode("latin-1")

    def decode(self, value):
        with io.BytesIO() as file:
            file.write(value.encode("latin-1"))
            file.seek(0)
            return np.load(file)


class NumpyConverterBase64(NumpyConverter):
    """Old numpy converter representation"""

    representation = "np.ndarray64"
    level = 2
