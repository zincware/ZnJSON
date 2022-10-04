"""Manage Converter Inputs based on available moduls"""
from znjson.converter.class_converter import ClassConverter
from znjson.converter.pathlib_converter import PathlibConverter

__all__ = ["PathlibConverter", "ClassConverter"]

try:
    from znjson.converter.numpy_converter_base64 import NumpyConverter
    from znjson.converter.numpy_converter_small import NumpyConverterSmall
    from znjson.converter.old_converters import (
        NumpyConverterBase64,
        NumpyConverterLatin1,
    )

    __all__ += [
        "NumpyConverterSmall",
        "NumpyConverter",
        "NumpyConverterBase64",
        "NumpyConverterLatin1",
    ]
except ModuleNotFoundError:
    pass
