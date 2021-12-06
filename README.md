# ZnJSON

Package to Encode/Decode some common file formats to json

Available via ``pip install znjson``

In comparison to `pickle` this allows having readable json files combined with some serialized data.

# Example

````python
import numpy as np
import json
import znjson

znjson.register(
    znjson.converter.NumpyConverter
)

data = json.dumps({"data": np.arange(9)}, cls=znjson.ZnEncoder)
_ = json.loads(data, cls=znjson.ZnDecoder)
````
