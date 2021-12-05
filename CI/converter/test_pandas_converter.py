import pandas as pd
import pytest
import json

import znconv

znconv.register(znconv.converter.PandasConverter)


@pytest.fixture
def pandas_dataframe():
    return pd.DataFrame({"foo": range(5), "bar": range(5, 10)})


def test_encode(pandas_dataframe):
    _ = json.dumps(pandas_dataframe, cls=znconv.ZnEncoder)


def test_decode(pandas_dataframe):
    encoded_str = json.dumps(pandas_dataframe, cls=znconv.ZnEncoder)
    pandas_dataframe.equals(json.loads(encoded_str, cls=znconv.ZnDecoder))
