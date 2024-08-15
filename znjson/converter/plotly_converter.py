import plotly.graph_objs
import plotly.io as pio

from znjson.base import ConverterBase


class PlotlyConverter(ConverterBase):
    instance = plotly.graph_objs.Figure
    representation = "plotly.graph_objs.Figure"
    level = 10

    def encode(self, obj):
        return obj.to_json()

    def decode(self, value):
        return pio.from_json(value)
