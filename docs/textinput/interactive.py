import dash_mantine_components as dmc
from lib.configurator import create_configurator

controls = [
    {
        "property": "placeholder",
        "component": "TextInput",
        "value": "Your Name",
        "placeholder": "Placeholder",
    },
    {
        "property": "label",
        "component": "TextInput",
        "value": "Full Name",
        "placeholder": "Label",
    },
    {"property": "description", "component": "TextInput", "placeholder": "Description"},
    {"property": "error", "component": "TextInput", "placeholder": "Error"},
    {"property": "size", "component": "DemoSlider", "value": "sm"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "required", "component": "Switch", "checked": True},
]

demo = dmc.TextInput(
    label="Full Name", placeholder="Your Name", style={"width": 300}, required=True
)

component = create_configurator(demo, controls)
