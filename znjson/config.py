from dataclasses import dataclass, field
from typing import List, Tuple, Type, Union

from znjson.base import ConverterBase


@dataclass()
class Config:
    ACTIVE_CONVERTER: List[Type[ConverterBase]] = field(default_factory=list)

    def sort(self):
        """Sort the ACTIVE_CONVERTER by their order"""
        sort = sorted([x() for x in self.ACTIVE_CONVERTER])
        self.ACTIVE_CONVERTER = list({type(x) for x in sort})


config = Config()


def register(
    obj: Union[
        List[Type[ConverterBase]], Tuple[Type[ConverterBase]], Type[ConverterBase]
    ],
    /,
):
    """register converters to be used with zn.En/DeCoder

    Updated the znconf.config which is used in the main converters
    """
    if isinstance(obj, (list, tuple)):
        config.ACTIVE_CONVERTER += obj
    else:
        config.ACTIVE_CONVERTER.append(obj)

    config.sort()


def deregister(
    obj: Union[
        List[Type[ConverterBase]], Tuple[Type[ConverterBase]], Type[ConverterBase]
    ],
    /,
):
    """remove the given zn.En/DeCoder from the config"""

    if isinstance(obj, (list, tuple)):
        [deregister(x) for x in obj]
    else:
        config.ACTIVE_CONVERTER = [x for x in config.ACTIVE_CONVERTER if x is not obj]
        config.sort()
