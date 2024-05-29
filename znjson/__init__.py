"""The ZnJSON serializing module

https://github.com/zincware/ZnJSON
"""

import importlib.metadata
import logging
import sys

from znjson import converter
from znjson.base import ConverterBase
from znjson.config import config, deregister, register
from znjson.main import ZnDecoder, ZnEncoder, dumps, loads

__all__ = [
    "ConverterBase",
    "ZnDecoder",
    "ZnEncoder",
    "config",
    "register",
    "deregister",
    "loads",
    "dumps",
]
__all__ += converter.__all__

__version__ = importlib.metadata.version("znjson")

config.register()

logger = logging.getLogger(__name__)
logger.setLevel(config.log_level)

# Formatter for advanced logging
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
formatter = logging.Formatter("%(asctime)s (%(levelname)s): %(message)s")

channel = logging.StreamHandler(sys.stdout)
channel.setLevel(logging.DEBUG)
channel.setFormatter(formatter)

logger.addHandler(channel)
