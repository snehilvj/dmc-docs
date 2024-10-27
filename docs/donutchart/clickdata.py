from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Stack(
    [
        dmc.DonutChart(id="figure-donutchart", data=data, withTooltip=False),
        dmc.Text(id="clickdata-donutchart1"),
        dmc.Text(id="clickdata-donutchart2"),
    ]
)



@callback(
    Output("clickdata-donutchart1", "children"),
    Output("clickdata-donutchart2", "children"),
    Input("figure-donutchart", "clickData"),
    Input("figure-donutchart", "clickSeriesName"),
)
def update(data, name):
    return f"clickData:  {data}", f"clickSeriesName: {name}"
