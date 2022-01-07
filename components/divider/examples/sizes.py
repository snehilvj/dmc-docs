import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Divider(size="xs"),
        dmc.Space(h=20),  # no-prism
        dmc.Divider(size="sm"),
        dmc.Space(h=20),  # no-prism
        dmc.Divider(size="md"),
        dmc.Space(h=20),  # no-prism
        dmc.Divider(size="lg"),
        dmc.Space(h=20),  # no-prism
        dmc.Divider(size="xl"),
        dmc.Space(h=20),  # no-prism
        dmc.Divider(size=10),
    ]
)
