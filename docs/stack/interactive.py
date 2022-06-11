import dash_mantine_components as dmc
from lib.configurator import create_configurator

aligns = {
    "Stretch": "stretch",
    "Center": "center",
    "Flex-End": "flex-end",
    "Flex-Start": "flex-start",
}

justifies = {
    "Space-between": "space-between",
    "Space-around": "space-around",
    "Center": "center",
    "Flex-End": "flex-end",
    "Flex-Start": "flex-start",
}

controls = [
    {
        "property": "align",
        "component": "Select",
        "data": [
            {"value": f"{value}", "label": f"{key}"} for key, value in aligns.items()
        ],
        "value": "center",
    },
    {
        "property": "justify",
        "component": "Select",
        "data": [
            {"value": f"{value}", "label": f"{key}"} for key, value in justifies.items()
        ],
        "value": "center",
    },
    {"property": "spacing", "component": "DemoSlider", "value": "sm"},
    {"property": "color", "component": "ColorPicker", "value": "#34c6ef5"},
]

demo = dmc.Stack(
    [
        dmc.Button("1", variant="outline"),
        dmc.Button("2", variant="outline"),
        dmc.Button("3", variant="outline"),
    ],
    align="flex-end",
    spacing="xl",
    justify="flex-start",
)

component = create_configurator(demo, controls)
