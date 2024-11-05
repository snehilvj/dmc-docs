from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Stack(
    [
        dmc.PieChart(
            id="figure-piechart-hover",
            data=data,
        ),
        dmc.Text(id="hoverdata-piechart1"),
        dmc.Text(id="hoverdata-piechart2"),
    ]
)


@callback(
    Output("hoverdata-piechart1", "children"),
    Output("hoverdata-piechart2", "children"),
    Input("figure-piechart-hover", "hoverData"),
    Input("figure-piechart-hover", "hoverSeriesName"),
)
def update(data, name):
    return f"hoverData:  {data}", f"hoverSeriesName: {name}"
