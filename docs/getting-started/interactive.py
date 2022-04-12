import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "variant",
        "component": "Select",
        "data": [
            "link",
            "filled",
            "outline",
            "light",
            "gradient",
            "white",
            "subtle",
            "default",
        ],
        "value": "filled",
    },
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {
        "property": "loading",
        "component": "Switch",
        "checked": False,
    },
]

demo = dmc.Button("Settings")

component = create_configurator(demo, controls)
