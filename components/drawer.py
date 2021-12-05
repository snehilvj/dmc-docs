import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

drawer = html.Div(
    [
        create_component_title("Drawer"),
        dmc.Drawer(
            id="drawer",
            padding="md",
            position="right",
            size=500,
            title="This is a drawer",
            children=[
                dmc.Button("Click me!"),
                dmc.Space(h=20),
                dmc.Select(
                    data=[
                        {"value": "react", "label": "React"},
                        {"value": "ng", "label": "Angular"},
                        {"value": "svelte", "label": "Svelte"},
                        {"value": "vue", "label": "Vue"},
                    ],
                    zIndex=1006,
                ),
                dmc.Space(h=20),
                dmc.DatePicker(zIndex=1005),
            ],
        ),
        dmc.Button("Toggle Drawer", id="drawer-button"),
        dmc.Space(h=30),
    ]
)
