"""Convert small numpy arrays to lists"""

import numpy as np

from znjson.base import ConverterBase


class NumpyConverterSmall(ConverterBase):
    """Convert small numpy arrays to lists"""

    instance = np.ndarray
    representation = "np.ndarray_small"
    level = 50

    def encode(self, obj):
        return obj.tolist()

    def decode(self, value):
        return np.array(value)

    def __eq__(self, other):
        if isinstance(other, self.instance):
            return len(np.shape(other)) == 1 and len(other) < 20
        return False
