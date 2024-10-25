import dash_mantine_components as dmc
from .data import data

component = dmc.LineChart(
    h=300,
    dataKey="date",
    data=data,
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"},
    ],
    withLegend=True,
    highlightHover=True,
    withTooltip=False
)
