import dash_mantine_components as dmc
from .data import data

component = dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    withGradient=True,
    series=[{"name": "Apples", "color": "var(--area-color)"}],
)

