"""The ZnJSON serializing module

https://github.com/zincware/ZnJSON
"""
import importlib.metadata

from znjson import converter
from znjson.base import ConverterBase
from znjson.config import config
from znjson.main import ZnDecoder, ZnEncoder

__all__ = ["ConverterBase", "ZnDecoder", "ZnEncoder", "config"]
__all__ += converter.__all__

__version__ = importlib.metadata.version("znjson")

config.register()
