import numpy as np

from znjson import ConverterBase


class SmallNumpyConverter(ConverterBase):
    instance = np.ndarray
    representation = "np.ndarray_small"
    level = 50

    def encode(self, obj):
        return obj.tolist()

    def decode(self, value):
        return np.array(value)

    def __eq__(self, other):
        return len(np.shape(other)) == 1 and len(other) < 20
