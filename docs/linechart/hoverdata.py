from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.LineChart(
            id="figure-linechart-hover",
            h=300,
            dataKey="date",
            data=data,
            series=[
                {"name": "Apples", "color": "indigo.6"},
                {"name": "Oranges", "color": "blue.6"},
                {"name": "Tomatoes", "color": "teal.6"},
            ],
            activeDotProps={"r": 8, "strokeWidth": 1, "fill": "#fff"},
            strokeWidth=4
        ),
        dmc.Text(id="hoverdata-linechart1"),
        dmc.Text(id="hoverdata-linechart2"),
    ]
)


@callback(
    Output("hoverdata-linechart1", "children"),
    Output("hoverdata-linechart2", "children"),
    Input("figure-linechart-hover", "hoverData"),
    Input("figure-linechart-hover", "hoverSeriesName"),
)
def update(data, name):
    return f"hoverData:  {data}", f"hoverSeriesName: {name}"

