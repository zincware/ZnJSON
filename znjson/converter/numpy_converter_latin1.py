import io

import numpy as np

from znjson import ConverterBase


class NumpyConverterLatin1(ConverterBase):
    """Do not use"""

    instance = np.ndarray
    representation = "np.ndarray"
    level = 0

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
