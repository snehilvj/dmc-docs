import dash_mantine_components as dmc
from .data import data

component = dmc.AreaChart(
    h=300,
    data=data,
    dataKey="date",
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"},
    ],
    referenceDots=[
        {"x": "Mar 25", "y": 3470, "color": "red.6", "label": "Peak"},
    ],
)
