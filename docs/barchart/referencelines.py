import dash_mantine_components as dmc
from .data import data

component = dmc.BarChart(
    h=300,
    dataKey="month",
    data=data,
    withTooltip=False,
    referenceLines=[
        {
            "y": 130,
            "color": "red.5",
            "label": "Profit reached",
            "labelPosition": "insideTopRight",
        }
    ],
    series=[
        {"name": "Smartphones", "color": "violet.6"},
        {"name": "Laptops", "color": "blue.6"},
        {"name": "Tablets", "color": "teal.6"},
    ],
)
