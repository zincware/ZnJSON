import pandas as pd
import pytest
import json

import znjson

znjson.register(znjson.converter.PandasConverter)


@pytest.fixture
def pandas_dataframe():
    return pd.DataFrame({"foo": range(5), "bar": range(5, 10)})


def test_encode(pandas_dataframe):
    _ = json.dumps(pandas_dataframe, cls=znjson.ZnEncoder)


def test_decode(pandas_dataframe):
    encoded_str = json.dumps(pandas_dataframe, cls=znjson.ZnEncoder)
    pandas_dataframe.equals(json.loads(encoded_str, cls=znjson.ZnDecoder))
