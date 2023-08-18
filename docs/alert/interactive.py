import dash_mantine_components as dmc
from dash_iconify import DashIconify

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker", "value": "#ff6b6b"},
    {"property": "withCloseButton", "component": "Switch", "checked": False},
    {
        "property": "variant",
        "component": "DemoSegmentedControl",
        "data": ["light", "filled", "outline"],
        "value": "light",
    },
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
]

demo = dmc.Alert(
    icon=DashIconify(icon="radix-icons:cross-circled"),
    title="Bummer",
    children="Something terrible happened! You made a mistake and there is no going back, your data was lost forever!",
    color="red",
)

component = create_configurator(demo, controls, center=False)
