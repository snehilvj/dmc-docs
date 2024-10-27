import dash_mantine_components as dmc
from .data import data

component = dmc.CompositeChart(
    h=300,
    data=data,
    dataKey="date",
    unit="$",
    maxBarWidth=30,
    series=[
        {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
        {"name": "Apples", "color": "red.8", "type": "line"},
        {"name": "Oranges", "color": "yellow.8", "type": "area"},
    ]
)
