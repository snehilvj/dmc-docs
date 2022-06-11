import dash_mantine_components as dmc
from dash import html
from lib.configurator import create_configurator
from dash_iconify import DashIconify

variants = {"Default": "default",
            "Filled": "filled",
            "Unstyled": "unstyled"}


controls = [
    {"property": "placeholder", "component": "TextInput", "value": "Password"},
    {"property": "description",
     "component": "TextInput",
     "value": "Password must include at least..",
     "style": {"width": 350}},
    {"property": "label", "component": "TextInput", "value": "Password"},
    {"property": "error", "component": "TextInput"},
    {
        "property": "variant",
        "component": "Select",
        "data": [
            {"value": f"{value}", "label": f"{key}"} for key, value in variants.items()
        ],
        "value": "default",
    },

    {"property": "size", "component": "DemoSlider", "value": "sm"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {"property": "disabled", "component": "Switch", "checked": False},
    {"property": "required", "component": "Switch", "checked": True},

]

demo = dmc.PasswordInput(
    icon=[DashIconify(icon='bi:shield-lock')],
    style={"width": 350})


component = create_configurator(demo, controls)
