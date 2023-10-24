import dash_mantine_components as dmc

component = dmc.MantineProvider(
    inherit=True,
    theme={
        "components": {
            "Badge": {
                "styles": {
                    "root": {"borderWidth": 1, "height": 30, "padding": 10},
                    "inner": {"fontWeight": 500},
                }
            }
        }
    },
    children=[dmc.Badge("Badge 1", variant="dot")],
)
