import dash_mantine_components as dmc
from dash import html

component = html.Div(
    style={"width": 300},
    children=dmc.BackgroundImage(
        src="https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?ixlib=rb-1.2.1&ixid"
        "=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=720&q=80",
        children=[
            dmc.Center(
                p="md",
                children=[
                    dmc.Text(
                        "BackgroundImage component can be used to add any content on image. It is used for cards, "
                        "hero headers and similar components",
                        color="yellow",
                    )
                ],
            )
        ],
    ),
)
