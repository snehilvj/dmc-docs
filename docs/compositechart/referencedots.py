import dash_mantine_components as dmc
from .data import data

component = dmc.CompositeChart(
    h=300,
    data=data,
    dataKey="date",
    maxBarWidth=30,
    series=[
        {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
        {"name": "Apples", "color": "red.8", "type": "line"},
    ],
    referenceDots=[
        {"x": "Mar 25", "y": 2764, "color": "red.8", "label": "Peak"},
    ],
)