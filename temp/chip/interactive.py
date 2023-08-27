import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {
        "property": "variant",
        "component": "DemoSegmentedControl",
        "data": ["outline", "filled"],
        "value": "outline",
    },
    {"property": "size", "component": "DemoSlider", "value": "sm"},
    {"property": "radius", "component": "DemoSlider", "value": "xl"},
]

demo = dmc.Chip("Dash Mantine Components", checked=True, variant="outline")

component = create_configurator(demo, controls)
