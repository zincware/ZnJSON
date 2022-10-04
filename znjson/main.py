"""ZnJSON main Encoder / Decoder classes to use with the default json library"""
import json
from typing import Any

from znjson.config import config


class SelectConverters:
    """Mixin to manipulate to converters in use"""

    _active_converters = None

    @classmethod
    def from_converters(cls, converter, add_default=False):
        """Return a new class definition with defined active converters

        Parameters
        ----------
        converter: converter|list of converters to use
        add_default: bool, default False
            In addition to the converter argument use the config.ACTIVE_CONVERTER as well

        Returns
        -------
        return a child class with altered _active_converters.
        ! This does not return an instance of the child class !
        """

        if not isinstance(converter, list):
            converter = [converter]

        class ZnEncoderCopy(cls):
            """Create a child of cls with altered _active_converters"""

            _active_converters = (
                converter + config.ACTIVE_CONVERTER if add_default else converter
            )

        return ZnEncoderCopy

    @property
    def active_converters(self) -> list:
        """Get the converters in use"""
        config.sort()
        if self._active_converters is None:
            return config.ACTIVE_CONVERTER
        return self._active_converters


class ZnEncoder(json.JSONEncoder, SelectConverters):
    """Encode objects using the ZnJSON Converter"""

    def default(self, o: Any) -> Any:
        for converter in self.active_converters:
            if converter() == o:
                return converter().encode_obj(o)
        raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")


class ZnDecoder(json.JSONDecoder, SelectConverters):
    """Decode data converted with ZnJSON encoder"""

    def __init__(self):
        super().__init__(object_hook=self._object_hook)

    def _object_hook(self, obj):
        """Object hook for decoding data in ZnDecoder"""
        try:
            # must have "_type" and "value" keys
            instance = obj["_type"]
            _ = obj["value"]
        except KeyError:
            return obj
        for converter in self.active_converters:
            if converter.representation == instance:
                return converter().decode_obj(obj)
        raise TypeError(f"Object of type {instance} could not be converted")


if __name__ == "__main__":
    import numpy as np

    import znjson

    znjson.config.register(znjson.converter.NumpyConverter)

    data = np.arange(10)

    print(json.dumps({"a": 5, "b": data}, cls=ZnEncoder))
    data_str = json.dumps({"a": 5, "b": data}, cls=ZnEncoder)
    print(json.loads(data_str, cls=ZnDecoder))
