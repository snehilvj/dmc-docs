import dash_mantine_components as dmc
from .data import data

component = dmc.CompositeChart(
    h=300,
    data=data,
    dataKey="date",
    withLegend=True,
    maxBarWidth=30,
    series=[
        {"name": "Apples", "color": "blue", "type": "line"},
    ]
)
