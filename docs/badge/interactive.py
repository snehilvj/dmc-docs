import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "variant",
        "component": "Select",
        "data": ["light", "filled", "outline", "dot", "gradient"],
        "value": "light",
    },
    {"property": "color", "component": "ColorPicker"},
    {"property": "size", "component": "DemoSlider", "value": "md"},
    {"property": "radius", "component": "DemoSlider", "value": "xl"},
]

demo = dmc.Badge("Badge")

component = create_configurator(demo, controls)
