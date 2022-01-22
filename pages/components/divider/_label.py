import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Divider(label="Click on update button to refresh"),
        dmc.Space(h=20),  # no-prism
        dmc.Divider(label="Divider with centered content", labelPosition="center"),
        dmc.Space(h=20),  # no-prism
        dmc.Divider(label="Divider with content on the right", labelPosition="right"),
    ]
)
