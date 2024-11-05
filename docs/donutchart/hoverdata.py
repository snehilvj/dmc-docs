from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Stack(
    [
        dmc.DonutChart(id="figure-donutchart-hover", data=data, withTooltip=False),
        dmc.Text(id="hoverdata-donutchart1"),
        dmc.Text(id="hoverdata-donutchart2"),
    ]
)


@callback(
    Output("hoverdata-donutchart1", "children"),
    Output("hoverdata-donutchart2", "children"),
    Input("figure-donutchart-hover", "hoverData"),
    Input("figure-donutchart-hover", "hoverSeriesName"),
)
def update(data, name):
    return f"hoverData:  {data}", f"hoverSeriesName: {name}"
