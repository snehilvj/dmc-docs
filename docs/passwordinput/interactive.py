import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "placeholder",
        "component": "TextInput",
        "value": "Password",
        "placeholder": "Placeholder",
    },
    {
        "property": "label",
        "component": "TextInput",
        "value": "Password",
        "placeholder": "Label",
    },
    {
        "property": "description",
        "component": "TextInput",
        "placeholder": "Description",
        "value": "Password must include at least one letter, number and special character",
    },
    {"property": "error", "component": "TextInput", "placeholder": "Error"},
    {"property": "size", "component": "DemoSlider", "value": "sm"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "required", "component": "Switch", "checked": True},
]

demo = dmc.PasswordInput(
    label="Password",
    placeholder="Password",
    description="Password must include at least one letter, number and special character",
    required=True,
)

component = create_configurator(demo, controls)
