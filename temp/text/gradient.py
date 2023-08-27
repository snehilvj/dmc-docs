import dash_mantine_components as dmc

component = dmc.Center(
    children=[
        dmc.Text(
            "Indigo cyan gradient",
            variant="gradient",
            gradient={"from": "red", "to": "yellow", "deg": 45},
            style={"fontSize": 40},
        )
    ]
)
