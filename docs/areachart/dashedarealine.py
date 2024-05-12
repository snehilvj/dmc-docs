
import dash_mantine_components as dmc
from .data import data

component = dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    type="stacked",
    strokeWidth=1,
    dotProps={"r": 2},
    activeDotProps={"r": 3, "strokeWidth": 1},
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6", "strokeDasharray": "5 5"}
    ]
)

