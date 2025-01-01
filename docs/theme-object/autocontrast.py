import dash_mantine_components as dmc

component = dmc.Box([
    dmc.Code("autoContrast=True"),
    dmc.Group(
        [
            dmc.Button("Lime.4 button", color="lime.4", autoContrast=True),
            dmc.Button("Blue.2 button", color="blue.2", autoContrast=True),
            dmc.Button("Orange.3 button", color="orange.3", autoContrast=True),
        ],
        mt="xs",
        mb="lg"
    ),
    dmc.Code("autoContrast=False"),
    dmc.Group(
        [
            dmc.Button("Lime.4 button", color="lime.4"),
            dmc.Button("Blue.2 button", color="blue.2"),
            dmc.Button("Orange.3 button", color="orange.3"),
        ],
        mt="xs"
    )
])