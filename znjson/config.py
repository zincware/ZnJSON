from dataclasses import dataclass, field
from typing import List, Tuple, Type, Union

from znjson.base import ConverterBase


@dataclass()
class Config:
    ACTIVE_CONVERTER: List[Type[ConverterBase]] = field(default_factory=list)

    def sort(self):
        """Sort the ACTIVE_CONVERTER by their order"""
        active_converters = set(self.ACTIVE_CONVERTER)
        sort = sorted([x() for x in active_converters])
        self.ACTIVE_CONVERTER = [type(x) for x in sort]


config = Config()


def register(
    obj: Union[
        List[Type[ConverterBase]], Tuple[Type[ConverterBase]], Type[ConverterBase]
    ] = None,
):
    """register converters to be used with zn.En/DeCoder

    Attributes
    ----------
    obj:
        If None, all available converters will be registered

    Updated the znconf.config which is used in the main converters
    """
    if obj is None:
        from znjson import converter

        [register(getattr(converter, name)) for name in converter.__all__]
        config.sort()
        return

    if isinstance(obj, (list, tuple)):
        config.ACTIVE_CONVERTER += obj
    else:
        config.ACTIVE_CONVERTER += [obj]

    config.sort()


def deregister(
    obj: Union[
        List[Type[ConverterBase]], Tuple[Type[ConverterBase]], Type[ConverterBase]
    ],
):
    """remove the given zn.En/DeCoder from the config"""

    if isinstance(obj, (list, tuple)):
        [deregister(x) for x in obj]
    else:
        config.ACTIVE_CONVERTER = [x for x in config.ACTIVE_CONVERTER if x is not obj]
        config.sort()
