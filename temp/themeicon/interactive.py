import dash_mantine_components as dmc
from dash_iconify import DashIconify

from lib.configurator import create_configurator

controls = [
    {
        "property": "variant",
        "component": "DemoSegmentedControl",
        "data": ["filled", "light", "outline"],
        "value": "filled",
    },
    {"property": "size", "component": "DemoSlider", "value": "md"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
]

demo = dmc.ThemeIcon(children=DashIconify(icon="tabler:photo"))

component = create_configurator(demo, controls)
