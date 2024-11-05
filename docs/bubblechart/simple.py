import dash_mantine_components as dmc
from .data import data


component = dmc.BubbleChart(
    gridColor="gray.5",
    textColor="gray.9",
    h=60,
    data=data,
    range=[16, 225],
    label="Sales/hour",
    color="lime.6",
    dataKey={"x": "hour", "y": "index", "z": "value"}
)