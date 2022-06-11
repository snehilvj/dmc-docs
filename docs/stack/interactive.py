import dash_mantine_components as dmc
from dash import html

from lib.configurator import create_configurator


controls = [
    {
        "property": "align",
        "component": "Select",
        "data": ["stretch", "center", "flex-end", "flex-start"],
        "value": "stretch",
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
        dmc.Button("1", fullWidth=True, variant="outline"),
        dmc.Button("2", fullWidth=True, variant="outline"),
        dmc.Button("3", fullWidth=True, variant="outline"),
    ],
    style={"height": 200},
    align="stretch",
    justify="center",
)

component = create_configurator(demo, controls, center=False)
