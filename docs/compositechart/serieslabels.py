import dash_mantine_components as dmc
from .data import data

component = dmc.CompositeChart(
    h=300,
    data=data,
    dataKey="date",
    withLegend=True,
    legendProps={"verticalAlign": "bottom"},
    maxBarWidth=30,
    series=[
        {
            "name": "Tomatoes",
            "label": "Tomatoes sales",
            "color": "rgba(18, 120, 255, 0.2)",
            "type": "bar",
        },
        {
            "name": "Apples",
            "label": "Apples sales",
            "color": "red.8",
            "type": "line",
        },
        {
            "name": "Oranges",
            "label": "Oranges sales",
            "color": "yellow.8",
            "type": "area",
        },
    ]
)
