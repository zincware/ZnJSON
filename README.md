[![Coverage Status](https://coveralls.io/repos/github/zincware/ZnJSON/badge.svg?branch=main)](https://coveralls.io/github/zincware/ZnJSON?branch=main)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black/)
[![Tests](https://github.com/zincware/ZnJSON/actions/workflows/pytest.yaml/badge.svg)](https://coveralls.io/github/zincware/ZnJSON?branch=main)
[![PyPI version](https://badge.fury.io/py/znjson.svg)](https://badge.fury.io/py/znjson)


# ZnJSON

Package to Encode/Decode some common file formats to json

Available via ``pip install znjson``

In comparison to `pickle` this allows having readable json files combined with some
serialized data.

# Example

````python
import numpy as np
import json
import znjson

data = json.dumps(
    obj={"data_np": np.arange(2), "data": [x for x in range(10)]},
    cls=znjson.ZnEncoder,
    indent=4
)
_ = json.loads(data, cls=znjson.ZnDecoder)
````
The resulting ``*.json`` file is partially readable and looks like this:

````json
{
    "data_np": {
        "_type": "np.ndarray_small",
        "value": [
            0,
            1
        ]
    },
    "data": [
        0,
        1,
        2,
        3,
        4
    ]
}
````

# Custom Converter

ZnJSON allows you to easily add custom converters.
Let's write a serializer for ``datetime.datetime``. 

````python
from znjson import ConverterBase
from datetime import datetime

class DatetimeConverter(ConverterBase):
    """Encode/Decode datetime objects

    Attributes
    ----------
    level: int
        Priority of this converter over others.
        A higher level will be used first, if there
        are multiple converters available
    representation: str
        An unique identifier for this converter.
    instance:
        Used to select the correct converter.
        This should fulfill isinstance(other, self.instance)
        or __eq__ should be overwritten.
    """
    level = 100
    representation = "datetime"
    instance = datetime

    def encode(self, obj: datetime) -> str:
        """Convert the datetime object to str / isoformat"""
        return obj.isoformat()
    def decode(self, value: str) -> datetime:
        """Create datetime object from str / isoformat"""
        return datetime.fromisoformat(value)
````

This allows us to use this new serializer:
````python
znjson.config.register(DatetimeConverter) # we need to register the new converter first
json_string = json.dumps(dt, cls=znjson.ZnEncoder, indent=4)
json.loads(json_string, cls=znjson.ZnDecoder)
````

and will result in
````json
{
    "_type": "datetime",
    "value": "2022-03-11T09:47:35.280331"
}
````

If you don't want to register your converter to be used everywhere, simply use:

```python
json_string = json.dumps(dt, cls=znjson.ZnEncoder.from_converters(DatetimeConverter))
```