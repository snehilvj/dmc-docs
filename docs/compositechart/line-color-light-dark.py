import dash_mantine_components as dmc
from .data import data

component = dmc.CompositeChart(
    h=300,
    dataKey="date",
    data=data,
    series=[{"name": "Apples", "color": "var(--chart-color)", "type": "line" }],
)

