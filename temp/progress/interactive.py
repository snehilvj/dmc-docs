import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "size", "component": "DemoSlider", "value": "md"},
    {
        "property": "value",
        "component": "NumberInput",
        "value": 69,
        "min": 0,
        "max": 100,
        "step": 10,
    },
    {"property": "striped", "component": "Switch", "checked": False},
    {"property": "animate", "component": "Switch", "checked": False},
]

demo = dmc.Progress(radius="sm", size="md", value=69)

component = create_configurator(demo, controls, center=False)
