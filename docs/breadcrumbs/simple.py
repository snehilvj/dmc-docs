import dash_mantine_components as dmc
from dash import dcc, html

component = html.Div(
    [
        # default separator
        dmc.Breadcrumbs(
            children=[
                dcc.Link("Home", href="/"),
                dcc.Link("Dash Mantine Components", href="/"),
                dcc.Link("Breadcrumbs", href="/components/breadcrumbs"),
            ],
        ),
        dmc.Space(h=20),
        # separator provided
        dmc.Breadcrumbs(
            separator="→",
            children=[
                dmc.Anchor("Home", href="/", underline=False),
                dmc.Anchor("Dash Mantine Components", href="/", underline=False),
                dmc.Anchor(
                    "Breadcrumbs", href="/components/breadcrumbs", underline=False
                ),
            ],
        ),
    ]
)
