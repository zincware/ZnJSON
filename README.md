# ZnConv

Package to Encode/Decode some common file formats to json

Available via ``pip install znconv``

In comparison to `pickle` this allows having readable json files combined with some serialized data.

# Example

````python
import numpy as np
import json
import znconv

znconv.register(
    znconv.converter.NumpyConverter
)

data = json.dumps({"data": np.arange(9)}, cls=znconv.ZnEncoder)
_ = json.loads(data, cls=znconv.ZnDecoder)
````
