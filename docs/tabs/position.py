import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {
        "property": "position",
        "component": "Select",
        "data": ["left", "right", "center", "apart"],
        "value": "left",
    },
    {
        "property": "variant",
        "component": "SegmentedControl",
        "data": [
            "default",
            "outline",
            "pills",
        ],
        "value": "default",
    },
    {"property": "grow", "component": "Switch", "checked": False},
]

demo = dmc.Tabs(
    [
        dmc.Tab("Gallery tab content", label="Gallery"),
        dmc.Tab("Messages tab content", label="Messages"),
        dmc.Tab("Settings tab content", label="Settings"),
    ]
)

component = create_configurator(demo, controls, center=False)
