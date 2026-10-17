import dash_mantine_components as dmc

component = dmc.Box(
    [
        dmc.Text("autoContrast: off"),
        dmc.Pagination(total=10, color="lime.4"),
        dmc.Text("autoContrast: on", mt="md"),
        dmc.Pagination(total=10, autoContrast=True, color="lime.4"),
    ]
)