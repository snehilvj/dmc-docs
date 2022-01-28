import dash_mantine_components as dmc

component = dmc.Center(
    style={"height": 200, "width": "100%"},
    children=[
        dmc.Badge("Free", style={"marginRight": 5}),
        dmc.Anchor(  # no-prism
            "Click now!", href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # no-prism
        ),  # no-prism
        dmc.Anchor("Click now!", href="https://mantine.dev/"),  # no-run
    ],
)
