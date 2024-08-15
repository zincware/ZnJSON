import plotly.express as px
import pytest
from plotly.graph_objs import Figure


@pytest.fixture
def plotly_figure():
    df = px.data.iris()
    return px.scatter(df, x="sepal_width", y="sepal_length")


def test_encode_plotly(plotly_figure):
    import znjson

    data = znjson.dumps(plotly_figure)
    assert data.startswith('{"_type": "plotly.graph_objs.Figure"')

    fig = znjson.loads(data)
    assert fig == plotly_figure
    assert isinstance(fig, Figure)

    assert fig.layout.xaxis.title.text == "sepal_width"
    assert fig.layout.yaxis.title.text == "sepal_length"


def test_encode_list_plotly(plotly_figure):
    import znjson

    data = znjson.dumps([plotly_figure, plotly_figure])
    assert data.startswith('[{"_type": "plotly.graph_objs.Figure"')

    fig = znjson.loads(data)
    assert fig == [plotly_figure, plotly_figure]
    assert isinstance(fig[0], Figure)
    assert isinstance(fig[1], Figure)

    assert fig[0].layout.xaxis.title.text == "sepal_width"
    assert fig[0].layout.yaxis.title.text == "sepal_length"
    assert fig[1].layout.xaxis.title.text == "sepal_width"
    assert fig[1].layout.yaxis.title.text == "sepal_length"
