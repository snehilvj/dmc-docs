from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.DonutChart(id="figure-donutchart", data=data, withTooltip=False),
        dmc.Text(id="clickdata-donutchart"),
    ]
)


@callback(
    Output("clickdata-donutchart", "children"),
    Input("figure-donutchart", "clickData"),
)
def update(clickdata):
    return str(clickdata)
