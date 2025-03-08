import dash_mantine_components as dmc
from .data import data

component = dmc.BubbleChart(
    h=60,
    data=data,
    range=[16, 225],
    label="Sales/hour",
    className="chart-grid-text-colors",
    dataKey={"x": "hour", "y": "index", "z": "value"}
)
