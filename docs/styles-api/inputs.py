import dash_mantine_components as dmc

component = dmc.MantineProvider(
    inherit=True,
    theme={
        "components": {
            "InputWrapper": {
                "styles": {
                    "label": {
                        "color": "blue",
                        "backgroundColor": dmc.theme.DEFAULT_COLORS["yellow"][1],
                    },
                }
            },
            "Input": {
                "styles": {
                    "input": {"borderColor": dmc.theme.DEFAULT_COLORS["violet"][4]}
                },
            },
        }
    },
    children=[
        dmc.TextInput(
            label="TextInput with custom styles",
            placeholder="TextInput with custom styles",
            description="Description below the input",
            w=300,
        )
    ],
)
