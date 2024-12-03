import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.NumberInput(label="By default controls are visible", w=250),
        dmc.NumberInput(
            label="Hide controls", hideControls=True, w=250
        ),
        dmc.NumberInput(
            label="Disabled and hide controls",
            disabled=True,
            hideControls=True,
            w=250,
        ),
    ]
)
