import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.TextInput(
            label="Success as boolean",
            placeholder="Success as boolean",
            success=True,
        ),
        dmc.TextInput(
            label="Success as React node",
            placeholder="Success as React node",
            success="Username is available",
        ),
    ],
)
