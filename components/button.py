from dash import html
import dash_mantine_components as dmc

from utils import create_component_title

button = html.Div(
    [
        create_component_title("Button"),
        dmc.Group(
            [
                dmc.Button("Click Me!"),
                dmc.Button("Click Me!", color="red"),
                dmc.Button("Click Me!", variant="outline"),
                dmc.Button(
                    "Click Me!",
                    variant="gradient",
                    gradient={"from": "teal", "to": "lime", "deg": 105},
                ),
                dmc.Button("Click Me!", loading=True),
                dmc.Button("Click Me!", compact=True),
                dmc.Button("Click Me!", radius="lg"),
                dmc.Button(["Click Me!", dmc.Space(w=9), dmc.Badge("5", id="badge")]),
            ]
        ),
        dmc.Space(h=30),
    ]
)
