import io

import numpy as np

from znjson import ConverterBase


class NumpyConverter(ConverterBase):
    instance = np.ndarray
    representation = "np.ndarray"
    order = 10

    def _encode(self, obj):
        with io.BytesIO() as f:
            np.save(f, obj)
            f.seek(0)
            return f.read().decode("latin-1")

    def _decode(self, value):
        with io.BytesIO() as f:
            f.write(value.encode("latin-1"))
            f.seek(0)
            return np.load(f)
