import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Checkbox(label="With boolean error", error=True),
        dmc.Checkbox(label="With error message", error="Must be checked"),
        dmc.Checkbox(
            label="With error message",
            error="No error styles",
            withErrorStyles=False,
        ),
    ]
)

