import dash_mantine_components as dmc
from .data import data


component = dmc.LineChart(
    h=300,
    dataKey="date",
    data=data,
    dotProps={"r": 6, "strokeWidth": 2, "stroke": "#fff"},
    activeDotProps={"r": 8, "strokeWidth": 1, "fill": "#fff"},
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"},
    ],
)
