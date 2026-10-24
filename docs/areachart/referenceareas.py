import dash_mantine_components as dmc
from .data import data

component = dmc.AreaChart(
    h=300,
    data=data,
    dataKey="date",
    type="stacked",
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"},
    ],
    referenceAreas=[
        {"x1": "Mar 23", "x2": "Mar 25", "color": "red.6", "label": "Weekend"},
    ],
)