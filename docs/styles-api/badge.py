import dash_mantine_components as dmc

component = dmc.Badge(
    "Badge 1",
    variant="dot",
    styles={
        "root": {"borderWidth": 1, "height": 30, "padding": 10},
        "inner": {"fontWeight": 500},
    },
)
