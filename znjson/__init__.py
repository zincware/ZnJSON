"""The ZnJSON serializing module

https://github.com/zincware/ZnJSON
"""
from znjson.base import ConverterBase
from znjson.config import config
from znjson.converter import *
from znjson.main import ZnDecoder, ZnEncoder

__all__ = ["ConverterBase", "ZnDecoder", "ZnEncoder", "config"]

__version__ = "0.1.2"

config.register()
