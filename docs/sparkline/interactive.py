import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Sparkline(w=200, h=60, data=[10, 20, 40, 20, 40, 10, 50])

configurator = Configurator(target)


configurator.add_select(
    "curveType",
    ["Bump", "Linear", "Natural", "Monotone", "Step", "StepBefore", "StepAfter"],
    "Linear",
)
configurator.add_colorpicker("color", "blue")
configurator.add_number_slider("fillOpacity", 1, min=0, max=1)
configurator.add_switch("withGradient", True)
configurator.add_number_slider("strokeWidth", 5, min=0.5, max=5)

component = configurator.panel
