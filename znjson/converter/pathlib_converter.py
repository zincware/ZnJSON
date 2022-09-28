"""Store pathlib as posix"""
import pathlib

from znjson import ConverterBase


class PathlibConverter(ConverterBase):
    instance = pathlib.Path
    representation = "pathlib.Path"
    level = 10

    def encode(self, obj: pathlib.Path):
        return obj.as_posix()

    def decode(self, value):
        return pathlib.Path(value)
