import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "size", "component": "DemoSlider", "value": "sm"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {
        "property": "disabled",
        "component": "Switch",
        "checked": False,
    },
]

demo = dmc.Checkbox(label="I agree to sell my privacy.", checked=True)

component = create_configurator(demo, controls)
