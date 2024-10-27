from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.BubbleChart(
            id="figure-bubblechart",
            gridColor="gray.5",
            textColor="gray.9",
            h=60,
            data=data,
            range=[16, 225],
            label="Sales/hour",
            color="lime.6",
            dataKey={"x": "hour", "y": "index", "z": "value"}
        ),
        dmc.Text(id="clickdata-bubblechart"),

    ]
)

@callback(
    Output("clickdata-bubblechart", "children"),
    Input("figure-bubblechart", "clickData"),
)
def update(data):
    return f"clickData:  {data}"

