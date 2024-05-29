"""Store pathlib as posix"""

import pathlib

from znjson.base import ConverterBase


class PathlibConverter(ConverterBase):
    """Store pathlib as posix"""

    instance = pathlib.Path
    representation = "pathlib.Path"
    level = 10

    def encode(self, obj: pathlib.Path):
        return obj.as_posix()

    def decode(self, value):
        return pathlib.Path(value)
