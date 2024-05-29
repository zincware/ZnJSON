"""Use pickle to serialize arbitrary classes"""

import functools
import importlib
import pickle

from znjson.base import ConverterBase


class ClassConverter(ConverterBase):
    """Converter using pickle to serialize arbitrary classes"""

    instance = object
    representation = "class"
    level = 0

    def encode(self, obj):
        return self.save_to_b64(method=functools.partial(pickle.dump, obj))

    def decode(self, value):
        return self.load_from_b64(value, pickle.load)

    def __eq__(self, other):
        try:
            return self._import(other.__module__, other.__class__.__name__) is not False
        except AttributeError:
            return False

    @staticmethod
    def _import(module, name):
        try:
            return getattr(importlib.import_module(module), name)
        except ImportError:
            return False
