import dash_mantine_components as dmc
from .data import data

component = dmc.CompositeChart(
    h=300,
    data=data,
    dataKey="date",
    dotProps={"r": 6, "strokeWidth": 2, "stroke": "#fff"},
    activeDotProps={"r": 8, "strokeWidth": 1, "fill": "#fff"},
    maxBarWidth=30,
    series=[
        {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
        {"name": "Apples", "color": "red.8", "type": "line"},
        {"name": "Oranges", "color": "yellow.8", "type": "area"},
    ]
)
