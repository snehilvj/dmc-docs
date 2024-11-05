from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Stack(
    [
        dmc.PieChart(
            id="figure-piechart",
            data=data,
        ),
        dmc.Text(id="clickdata-piechart1"),
        dmc.Text(id="clickdata-piechart2"),
    ]
)


@callback(
    Output("clickdata-piechart1", "children"),
    Output("clickdata-piechart2", "children"),
    Input("figure-piechart", "clickData"),
    Input("figure-piechart", "clickSeriesName"),
)
def update(data, name):
    return f"clickData:  {data}", f"clickSeriesName: {name}"
