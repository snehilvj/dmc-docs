from dash import html
import dash_mantine_components as dmc

from utils import create_component_title


affix = html.Div(
    [
        create_component_title("Affix"),
        dmc.Affix(
            dmc.Button("I'm in an Affix Component"),
            position={"bottom": 20, "right": 20},
        ),
        dmc.Text("Look at the bottom right!"),
        dmc.Space(h=30),
    ]
)
