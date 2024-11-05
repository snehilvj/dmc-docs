from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.CompositeChart(
            id="figure-compositechart-hover",
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
        dmc.Text(id="hoverdata-compositechart1"),
        dmc.Text(id="hoverdata-compositechart2"),
    ]
)

@callback(
    Output("hoverdata-compositechart1", "children"),
    Output("hoverdata-compositechart2", "children"),
    Input("figure-compositechart-hover", "hoverData"),
    Input("figure-compositechart-hover", "hoverSeriesName"),
)
def update(data, name):
    return f"hoverData:  {data}", f"hoverSeriesName: {name}"

