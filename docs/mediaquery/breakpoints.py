import dash_mantine_components as dmc

highlight = {"border": f"1px solid {dmc.theme.DEFAULT_COLORS['blue'][3]}"}

component = dmc.Group(
    direction="column",
    spacing=5,
    children=[
        dmc.MediaQuery("larger than lg", largerThan="lg", styles=highlight),
        dmc.MediaQuery("smaller than lg", smallerThan="lg", styles=highlight),
        dmc.MediaQuery(
            "smaller than xl, larger than sm",
            smallerThan="xl",
            largerThan="sm",
            styles=highlight,
        ),
        dmc.MediaQuery(
            "smaller than 1500, larger than 800",
            smallerThan=1500,
            largerThan=800,
            styles=highlight,
        ),
    ],
)
