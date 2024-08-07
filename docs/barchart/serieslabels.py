import dash_mantine_components as dmc
from .data import data

component = dmc.BarChart(
    h=300,
    dataKey="month",
    data=data,
    type="stacked",
    withLegend=True,
    legendProps={"verticalAlign": "bottom"},
    series=[
        {"name": "Smartphones", "label": "Smartphones sales", "color": "violet.6"},
        {"name": "Laptops", "label": "Laptops sales", "color": "blue.6"},
        {"name": "Tablets", "label": "Tablets sales", "color": "teal.6"},
    ],
)
