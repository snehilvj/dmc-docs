import dash_mantine_components as dmc
from dash import html

from lib.configurator import create_configurator


controls = [
    {
        "property": "align",
        "component": "Select",
        "data": ["stretch", "center", "flex-end", "flex-start"],
        "value": "flex-start",
    },
    {
        "property": "justify",
        "component": "Select",
        "data": ["space-between", "space-around", "center", "flex-end", "flex-start"],
        "value": "center",
    },
    {"property": "spacing", "component": "DemoSlider", "value": "sm"},
]

demo = dmc.Stack(
    [
        dmc.Button("1", variant="outline"),
        dmc.Button("2", variant="outline"),
        dmc.Button("3", variant="outline"),
    ],
    style={"height": 200},
    align="flex-start",
    justify="center",
)

component = create_configurator(demo, controls, center=False)
