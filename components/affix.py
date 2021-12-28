import dash_mantine_components as dmc
from dash import html

title = "Affix"
doc = dmc.Affix.__doc__

layout = html.Div(
    children=[
        dmc.Text("Simple", color="dimmed"),
        dmc.Space(h=10),
        dmc.Affix(
            dmc.Button("I'm in an Affix Component"),
            position={"bottom": 20, "right": 20},
        ),
        dmc.Text("Look at the bottom right!"),
    ]
)
