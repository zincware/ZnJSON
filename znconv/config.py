from .base import ConverterBase
from typing import List, Type, Union, Tuple
from dataclasses import dataclass, field


@dataclass()
class Config:
    ACTIVE_CONVERTER: List[Type[ConverterBase]] = field(default_factory=list)


config = Config()


def register(
    obj: Union[
        List[Type[ConverterBase]], Tuple[Type[ConverterBase]], Type[ConverterBase]
    ]
):
    """register converters to be used with zn.En/DeCoder

    Updated the znconf.config which is used in the main converters
    """
    if isinstance(obj, list):
        config.ACTIVE_CONVERTER += obj
    elif isinstance(obj, tuple):
        config.ACTIVE_CONVERTER += obj
    config.ACTIVE_CONVERTER.append(obj)
