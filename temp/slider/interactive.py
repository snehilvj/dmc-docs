import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "size", "component": "DemoSlider", "value": "md"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "showLabelOnHover", "component": "Switch", "checked": True},
    {"property": "labelAlwaysOn", "component": "Switch", "checked": False},
]

demo = dmc.Slider(
    value=69,
    updatemode="mouseup",
    marks=[
        {"value": 20, "label": "20%"},
        {"value": 50, "label": "50%"},
        {"value": 80, "label": "80%"},
    ],
)

component = create_configurator(demo, controls, center=False)
