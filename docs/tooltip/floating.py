import dash_mantine_components as dmc

component = dmc.Center(
    [
        dmc.FloatingTooltip(
            label="Tooltip",
            color="orange",
            children=[
                dmc.Center(
                    dmc.Text("Hover over the box to see tooltip"),
                    style={
                        "height": 100,
                        "padding": 10,
                        "border": "2px solid  var(--mantine-color-gray-6)",
                    },
                )
            ],
        )
    ]
)
