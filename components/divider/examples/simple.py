import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Divider(variant="solid"),
        dmc.Space(h=20),  # no-prism
        dmc.Divider(variant="dashed"),
        dmc.Space(h=20),  # no-prism
        dmc.Divider(variant="dotted"),
    ]
)
