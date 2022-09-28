"""ZnJSON main Encoder / Decoder classes to use with the default json library"""
import json
from typing import Any

from znjson.config import config


class ZnEncoder(json.JSONEncoder):
    """Encode objects using the ZnJSON Converter"""

    def default(self, o: Any) -> Any:
        config.sort()
        for converter in config.ACTIVE_CONVERTER:
            if converter() == o:
                return converter().encode_obj(o)
        raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")


def object_hook(obj):
    """Object hook for decoding data in ZnDecoder"""
    try:
        # must have "_type" and "value" keys
        instance = obj["_type"]
        _ = obj["value"]
    except KeyError:
        return obj
    config.sort()
    for converter in config.ACTIVE_CONVERTER:
        if converter.representation == instance:
            return converter().decode_obj(obj)
    raise TypeError(f"Object of type {instance} could not be converted")


class ZnDecoder(json.JSONDecoder):
    """Decode data converted with ZnJSON encoder"""

    def __init__(self):
        super().__init__(object_hook=object_hook)


if __name__ == "__main__":
    import numpy as np

    import znjson

    znjson.config.register(znjson.converter.NumpyConverter)

    data = np.arange(10)

    print(json.dumps({"a": 5, "b": data}, cls=ZnEncoder))
    data_str = json.dumps({"a": 5, "b": data}, cls=ZnEncoder)
    print(json.loads(data_str, cls=ZnDecoder))
