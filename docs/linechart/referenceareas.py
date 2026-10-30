import dash_mantine_components as dmc
from .data import data

component = dmc.LineChart(
    h=300,
    data=data,
    dataKey="date",
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"},
    ],
    referenceAreas=[
        {"y1": 2000, "y2": 3000, "color": "teal.6", "label": "Target range"},
    ],
)