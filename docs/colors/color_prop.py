import dash_mantine_components as dmc

component= dmc.Box([
    dmc.Text("Filled variant", size="sm", mb=5, fw=500),
    dmc.Group([
        dmc.Button("Theme color", color="cyan"),
        dmc.Button("Hex color", color="#1D72FE")
    ]),

    dmc.Text("Light variant", size="sm", mb=5, mt="md", fw=500),
    dmc.Group([
        dmc.Button("Theme color", variant="light", color="cyan"),
        dmc.Button("Hex color", variant="light", color="#1D72FE")
    ]),

    dmc.Text("Outline variant", size="sm", mb=5, mt="md", fw=500),
    dmc.Group([
        dmc.Button("Theme color", variant="outline", color="cyan"),
        dmc.Button("Hex color", variant="outline", color="#1D72FE")
    ])
])
