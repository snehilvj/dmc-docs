import dash_mantine_components as dmc

component = dmc.Button(
    children=[
        "Notifications", dmc.Badge("2", radius="sm", style={"marginLeft": 7})
    ]
)
