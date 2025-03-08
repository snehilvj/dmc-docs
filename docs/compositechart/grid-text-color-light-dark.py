import dash_mantine_components as dmc
from .data import data

component = dmc.CompositeChart(
    h=300,
    dataKey="date",
    data=data,
    maxBarWidth=30,
    className="chart-grid-text-colors",
    series=[
        {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
        {"name": "Apples", "color": "red.8", "type": "line"},
        {"name": "Oranges", "color": "yellow.8", "type": "area"},
    ]
)
