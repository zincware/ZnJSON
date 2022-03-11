import pathlib

from znjson import ConverterBase


class PathlibConverter(ConverterBase):
    instance = pathlib.Path
    representation = "pathlib.Path"
    level = 10

    def _encode(self, obj: pathlib.Path):
        return obj.as_posix()

    def _decode(self, value):
        return pathlib.Path(value)
