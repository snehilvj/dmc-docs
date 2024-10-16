import dash_mantine_components as dmc
from .data import data

component = dmc.BarChart(
    h=300,
    dataKey="month",
    data=data,
    series=[
        {"name": "Smartphones", "color": "violet.6", "stackId": "a"},
        {"name": "Laptops", "color": "blue.6", "stackId": "b"},
        {"name": "Tablets", "color": "teal.6", "stackId": "b"},
    ],
)
