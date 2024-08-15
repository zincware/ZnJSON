"""Manage Converter Inputs based on available moduls"""

from znjson.converter.class_converter import ClassConverter
from znjson.converter.pathlib_converter import PathlibConverter
import contextlib

__all__ = ["PathlibConverter", "ClassConverter"]

with contextlib.suppress(ModuleNotFoundError):
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


with contextlib.suppress(ModuleNotFoundError):
    from znjson.converter.plotly_converter import PlotlyConverter

    __all__ += ["PlotlyConverter"]
