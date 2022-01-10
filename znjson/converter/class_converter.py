import importlib
import io
import pickle

from znjson import ConverterBase


class ClassConverter(ConverterBase):
    instance = object
    representation = "class"
    order = 100

    def _encode(self, obj):
        with io.BytesIO() as f:
            pickle.dump(obj, file=f)
            f.seek(0)
            return f.read().decode("latin-1")

    def _decode(self, value):
        with io.BytesIO() as f:
            f.write(value.encode("latin-1"))
            f.seek(0)
            return pickle.load(f)

    def __eq__(self, other):
        return self._import(other.__module__, other.__class__.__name__) is not False

    @staticmethod
    def _import(module, name):
        try:
            return getattr(importlib.import_module(module), name)
        except ImportError:
            return False
