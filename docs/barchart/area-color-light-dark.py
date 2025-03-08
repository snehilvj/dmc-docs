import dash_mantine_components as dmc
from .data import data

component = dmc.BarChart(
    h=300,
    dataKey="date",
    data=data,
    series=[{"name": "Smartphones", "color": "var(--area-color)"}],
)