from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.CompositeChart(
            id="figure-compositechart",
            h=300,
            data=data,
            dataKey="date",
            withLegend=True,
            maxBarWidth=30,
            series=[
                {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
                {"name": "Apples", "color": "red.8", "type": "line"},
                {"name": "Oranges", "color": "yellow.8", "type": "area"},
            ]
        ),
        dmc.Text(id="clickdata-compositechart1"),
        dmc.Text(id="clickdata-compositechart2"),
    ]
)

@callback(
    Output("clickdata-compositechart1", "children"),
    Output("clickdata-compositechart2", "children"),
    Input("figure-compositechart", "clickData"),
    Input("figure-compositechart", "clickSeriesName"),
)
def update(data, name):
    return f"clickData:  {data}", f"clickSeriesName: {name}"

