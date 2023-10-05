import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-slider"

target = dmc.Slider(
    value=69,
    updatemode="mouseup",
    marks=[
        {"value": 20, "label": "20%"},
        {"value": 50, "label": "50%"},
        {"value": 80, "label": "80%"},
    ],
    id=TARGET_ID,
)

configurator = Configurator(target, TARGET_ID)

configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "lg")
configurator.add_switch("showLabelOnHover", True)
configurator.add_switch("labelAlwaysOn", False)

component = configurator.panel
