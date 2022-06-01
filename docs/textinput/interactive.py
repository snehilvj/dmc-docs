import dash_mantine_components as dmc
from lib.configurator import create_configurator

controls = [
    {"property": "placeholder", "component": "TextInput", "placeholder": "Your Name"},
    {"property": "description", "component": "TextInput", "description": "Description"},
    {"property": "error", "component": "TextInput"},
    {
        "property": "variant",
        "component": "Select",
        "data": [
            {"value": "default", "label": "Default"},
            {"value": "filled", "label": "Filled"},
            {"value": "unstyled", "label": "Unstyled"},
            {"value": "headless", "label": "Headless"},
        ],
        "value": "default",
    },
    {"property": "size", "component": "DemoSlider", "value": "sm"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "disabled", "component": "Switch", "checked": False},
    {"property": "required", "component": "Switch", "checked": True},

]

demo = dmc.TextInput(
    label='Full name',
    placeholder='Your name'
)

component = create_configurator(demo, controls)