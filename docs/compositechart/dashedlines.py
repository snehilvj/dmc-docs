import dash_mantine_components as dmc
from .data import data

component = dmc.CompositeChart(
    h=300,
    data=data,
    dataKey="date",
    strokeWidth=1,
    dotProps={"r": 2},
    activeDotProps={"r": 3, "strokeWidth": 1},
    maxBarWidth=30,
    series=[
        {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
        {"name": "Apples", "color": "red.8", "type": "line", "strokeDasharray": "5 5"},
        {"name": "Oranges", "color": "yellow.8", "type": "area", "strokeDasharray": "5 5"},
    ]
)