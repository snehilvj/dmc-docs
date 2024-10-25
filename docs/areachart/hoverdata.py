from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data


component = dmc.Group(
    [
        dmc.AreaChart(
            id="figure-areachart-hover",
            h=300,
            dataKey="date",
            data=data,
            type="stacked",
            series=[
                {"name": "Apples", "color": "indigo.6"},
                {"name": "Oranges", "color": "blue.6"},
                {"name": "Tomatoes", "color": "teal.6"},
            ],
        ),
        dmc.Text(id="hoverdata-areachart1"),
        dmc.Text(id="hoverdata-areachart2"),
    ]
)


@callback(
    Output("hoverdata-areachart1", "children"),
    Output("hoverdata-areachart2", "children"),
    Input("figure-areachart-hover", "hoverData"),
    Input("figure-areachart-hover", "hoverSeriesName"),
)
def update(data, name):
    return f"hoverData:  {data}", f"hoverSeriesName: {name}"

