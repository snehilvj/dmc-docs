import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.NumberInput(
            label="By default controls are visible",
            style={"width": 250},
        ),
        dmc.NumberInput(
            label="Disable with hideControls prop",
            hideControls=True,
            style={"width": 250},
        ),
        dmc.NumberInput(
            label="Controls are also not rendered when input is disabled",
            disabled=True,
            style={"width": 250},
        ),
    ]
)
