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
    ] = None,
    /,
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

        all_converters = [getattr(converter, name) for name in converter.__all__]
        register(all_converters)
        config.sort()
        return

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
