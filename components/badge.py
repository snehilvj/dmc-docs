from dash import html
import dash_mantine_components as dmc

from utils import create_component_title

badge = html.Div(
    [
        create_component_title("Badge"),
        dmc.Group(
            [
                dmc.Badge("Click Me!"),
                dmc.Badge("Click Me!", color="red"),
                dmc.Badge("Click Me!", variant="outline"),
                dmc.Badge("Click Me!", variant="dot"),
                dmc.Badge(
                    "Click Me!",
                    variant="gradient",
                    gradient={"from": "teal", "to": "lime", "deg": 105},
                ),
                dmc.Badge("Click Me!", radius="xs"),
            ]
        ),
        dmc.Space(h=30),
    ]
)
