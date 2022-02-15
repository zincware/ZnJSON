import json
from typing import Any

from znjson.config import config


class ZnEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        config.sort()
        for converter in config.ACTIVE_CONVERTER:
            if converter() == o:
                return converter().encode(o)
        raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")


class ZnDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.object_hook)

    def object_hook(self, obj):
        try:
            # must have "_type" and "value" keys
            instance = obj["_type"]
            _ = obj["value"]
        except KeyError:
            return obj
        config.sort()
        for converter in config.ACTIVE_CONVERTER:
            if converter.representation == instance:
                return converter().decode(obj)
        raise TypeError(f"Object of type {instance} could not be converted")


if __name__ == "__main__":
    import numpy as np

    import znjson

    znjson.register(znjson.converter.NumpyConverter)

    data = np.arange(10)

    print(json.dumps({"a": 5, "b": data}, cls=ZnEncoder))
    data_str = json.dumps({"a": 5, "b": data}, cls=ZnEncoder)
    print(json.loads(data_str, cls=ZnDecoder))
