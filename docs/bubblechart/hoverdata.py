from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.BubbleChart(
            id="figure-bubblechart-hover",
            gridColor="gray.5",
            textColor="gray.9",
            h=60,
            data=data,
            range=[16, 225],
            label="Sales/hour",
            color="lime.6",
            dataKey={"x": "hour", "y": "index", "z": "value"}
        ),
        dmc.Text(id="hoverdata-bubblechart"),

    ]
)

@callback(
    Output("hoverdata-bubblechart", "children"),
    Input("figure-bubblechart-hover", "hoverData"),
)
def update(data):
    return f"hoverData:  {data}"

