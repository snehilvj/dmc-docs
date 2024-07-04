import dash_mantine_components as dmc
from .data import data

from lib.configurator import Configurator

target = dmc.BarChart(
    h=300,
    dataKey="month",
    data=data,
    series=[
        {"name": "Smartphones", "color": "violet.6"},
        {"name": "Laptops", "color": "blue.6"},
        {"name": "Tablets", "color": "teal.6"}
    ],
    tickLine="y",

)

configurator = Configurator(target)

configurator.add_segmented_control("tickLine", ["x", "y", "xy", "none"], "xy")
configurator.add_segmented_control("gridAxis", ["x", "y", "xy", "none"], "x")
configurator.add_switch("withXAxis", True)
configurator.add_switch("withYAxis", True)



component = configurator.panel

