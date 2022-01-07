from dataclasses import dataclass, field
from typing import List, Tuple, Type, Union

from .base import ConverterBase


@dataclass()
class Config:
    ACTIVE_CONVERTER: List[Type[ConverterBase]] = field(default_factory=list)


config = Config()


def register(
    obj: Union[List[Type[ConverterBase]], Tuple[Type[ConverterBase]], Type[ConverterBase]]
):
    """register converters to be used with zn.En/DeCoder

    Updated the znconf.config which is used in the main converters
    """
    if isinstance(obj, list):
        config.ACTIVE_CONVERTER += obj
    elif isinstance(obj, tuple):
        config.ACTIVE_CONVERTER += obj
    config.ACTIVE_CONVERTER.append(obj)
