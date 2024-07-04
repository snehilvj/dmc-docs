
import dash_mantine_components as dmc
from .data import data

component = dmc.LineChart(
    h=300,
    dataKey="date",
    data=data,
    withLegend=True,
    legendProps={"verticalAlign": "bottom"},
    series=[
        {"name": "Apples", "label": "Apples sales", "color": "indigo.6"},
        {"name": "Oranges", "label": "Oranges sales", "color": "blue.6"},
        {"name": "Tomatoes", "label": "Tomatoes sales", "color": "teal.6"}
    ]
)
