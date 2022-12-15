import dash_mantine_components as dmc
from dash_iconify import DashIconify

from lib.configurator import create_configurator

controls = [
    {
        "property": "variant",
        "component": "Select",
        "data": ["filled", "outline", "light", "subtle", "default", "transparent"],
        "value": "filled",
    },
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "size", "component": "DemoSlider", "value": "lg"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "loading", "component": "Switch", "checked": False},
    {"property": "disabled", "component": "Switch", "checked": False},
]

demo = dmc.ActionIcon(
    DashIconify(icon="clarity:settings-line", width=20), size="lg", variant="filled"
)

component = create_configurator(demo, controls)
