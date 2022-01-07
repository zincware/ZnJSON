[![Coverage Status](https://coveralls.io/repos/github/zincware/ZnJSON/badge.svg?branch=main)](https://coveralls.io/github/zincware/ZnJSON?branch=main)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black/)
[![Tests](https://github.com/zincware/ZnJSON/actions/workflows/pytest.yaml/badge.svg)](https://coveralls.io/github/zincware/ZnJSON?branch=main)

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

znjson.register(
    znjson.converter.NumpyConverter
)

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
        "_type": "np.ndarray",
        "value": "\u0093NUMPY\u0001\u0000v\u0000{'descr': '<i4', 'fortran_order': False, 'shape': (2,), }                                                            \n\u0000\u0000\u0000\u0000\u0001\u0000\u0000\u0000"
    },
    "data": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
    ]
}
````