import dash_mantine_components as dmc
from .data import data

from lib.configurator import Configurator

target =dmc.CompositeChart(
    h=300,
    data=data,
    dataKey="date",
    withLegend=True,
    maxBarWidth=30,
    series=[
        {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
        {"name": "Apples", "color": "red.8", "type": "line"},
        {"name": "Oranges", "color": "yellow.8", "type": "area"},
    ]
)

configurator = Configurator(target)


configurator.add_select(
    "curveType",
    ["Bump", "Linear", "Natural", "Monotone", "Step", "StepBefore", "StepAfter"],
    "Linear",
)

configurator.add_segmented_control("tickLine", ["x", "y", "xy", "none"], "xy")
configurator.add_segmented_control("gridAxis", ["x", "y", "xy", "none"], "x")
configurator.add_switch("withXAxis", True)
configurator.add_switch("withYAxis", True)


component = configurator.panel
