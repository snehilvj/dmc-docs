import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Toggle("Save", autoWidth=True),
        dmc.Toggle("Active", autoWidth=True, active=True),
        dmc.Toggle("Disabled", autoWidth=True, disabled=True),
    ]
)
