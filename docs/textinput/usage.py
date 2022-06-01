import dash_mantine_components as dmc
from lib.configurator import create_configurator

controls = [
    {"property": "size", "component": "DemoSlider", "value": "sm"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "disabled", "component": "Switch", "checked": False},
    {"property": "required", "component": "Switch", "checked": False},
]

demo = dmc.TextInput(
    label='Full name',
    placeholder='Your name'
)

component = create_configurator(demo, controls)