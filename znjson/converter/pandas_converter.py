import io

import pandas

from znjson import ConverterBase


class PandasConverter(ConverterBase):
    instance = pandas.DataFrame
    representation = "pandas.DataFrame"

    def _encode(self, obj: pandas.DataFrame):
        with io.BytesIO() as f:
            obj.to_pickle(f)
            f.seek(0)
            return f.read().decode("latin-1")

    def _decode(self, value):
        with io.BytesIO() as f:
            f.write(value.encode("latin-1"))
            f.seek(0)
            return pandas.read_pickle(f)
