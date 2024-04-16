import dash_mantine_components as dmc

component = dmc.Center(
    style={"height": 200, "width": "100%"},
    children=[
        dmc.Badge("Free", style={"marginRight": 5}),
        dmc.Anchor("Click now!", href="https://mantine.dev/"),
    ],
)
