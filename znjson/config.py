"""ZnJSON global configuration file"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Type, Union

from znjson import converter
from znjson.base import ConverterBase
from znjson.exceptions import NonUniqueRepresentation

log = logging.getLogger(__name__)


@dataclass()
class Config:
    """ZnJSON global config object"""

    ACTIVE_CONVERTER: List[Type[ConverterBase]] = field(  # pylint: disable=C0103
        default_factory=list
    )
    log_level: int = logging.WARNING

    def sort(self):
        """Sort the ACTIVE_CONVERTER by their level

        Start from high levels to low levels
        """
        active_converter = set(self.ACTIVE_CONVERTER)
        active_converter = sorted([x() for x in active_converter], reverse=True)
        self.ACTIVE_CONVERTER = [type(x) for x in active_converter]

    def register(
        self,
        obj: Optional[
            Union[
                List[Type[ConverterBase]],
                Tuple[Type[ConverterBase]],
                Type[ConverterBase],
            ]
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
            # register all default converters
            for name in converter.__all__:
                self.register(getattr(converter, name))
            self.sort()
            return

        if isinstance(obj, (list, tuple)):
            obj = set(obj)  # remove true duplicates
            if len({x.representation for x in obj}) != len(obj):
                raise NonUniqueRepresentation(
                    "Can not register multiple converters with the same representation"
                    " string."
                )
            self.ACTIVE_CONVERTER += obj
        else:
            self.ACTIVE_CONVERTER += [obj]

        self.sort()

    def deregister(
        self,
        obj: Union[
            List[Type[ConverterBase]], Tuple[Type[ConverterBase]], Type[ConverterBase]
        ],
    ):
        """remove the given zn.En/DeCoder from the config"""

        if isinstance(obj, (list, tuple)):
            for converter_type in obj:
                self.deregister(converter_type)
        else:
            self.ACTIVE_CONVERTER = [x for x in self.ACTIVE_CONVERTER if x is not obj]
            self.sort()


config = Config()


def register(obj=None):
    """Depreciated register method"""
    log.warning(
        "DEPRECATED: 'register()' is deprecated, use 'config.register()' instead."
    )
    config.register(obj)


def deregister(obj):
    """Depreciated deregister method"""
    log.warning(
        "DEPRECATED: 'deregister()' is deprecated, use 'config.deregister()' instead."
    )
    config.deregister(obj)
