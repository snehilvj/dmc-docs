from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.PieChart(
            id="figure-piechart",
            data=data,
        ),
        dmc.Text(id="clickdata-piechart"),
    ]
)


@callback(
    Output("clickdata-piechart", "children"),
    Input("figure-piechart", "clickData"),
)
def update(clickdata):
    return str(clickdata)
