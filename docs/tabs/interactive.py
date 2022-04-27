import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
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
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
    {"property": "tabPadding", "component": "DemoSlider", "value": "xs"},
    {
        "property": "orientation",
        "component": "SegmentedControl",
        "data": [
            "horizontal",
            "vertical",
        ],
        "value": "horizontal",
    },
]

demo = dmc.Tabs(
    [
        dmc.Tab("Gallery tab content", label="Gallery"),
        dmc.Tab("Messages tab content", label="Messages"),
        dmc.Tab("Settings tab content", label="Settings"),
    ]
)

component = create_configurator(demo, controls, center=False)
