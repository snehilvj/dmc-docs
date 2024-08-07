import dash_mantine_components as dmc
from .data import data
from lib.configurator import Configurator

target = dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"},
    ],
    curveType="linear",
    tickLine="xy",
    withGradient=False,
    withXAxis=False,
    withDots=False,
)

configurator = Configurator(target)

configurator.add_select(
    "curveType",
    ["Bump", "Linear", "Natural", "Monotone", "Step", "StepBefore", "StepAfter"],
    "Monotone",
)

configurator.add_segmented_control("tickLine", ["x", "y", "xy", "none"], "xy")
configurator.add_segmented_control("gridAxis", ["x", "y", "xy", "none"], "x")
configurator.add_switch("withGradient", False)
configurator.add_switch("withXAxis", False)
configurator.add_switch("withYAxis", False)
configurator.add_switch("withDots", False)


component = configurator.panel
