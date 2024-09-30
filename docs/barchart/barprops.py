import dash_mantine_components as dmc
from .data import data

component = dmc.BarChart(
    h=300,
    dataKey="month",
    data=data,
    orientation="vertical",
    yAxisProps={"width": 80},
    barProps={"radius": 50},
    series=[{"name": "Smartphones", "color": "violet.6"}],
)
