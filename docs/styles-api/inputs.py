import dash_mantine_components as dmc

component = dmc.MantineProvider(
    theme={
        "components": {
            "InputWrapper": {
                "styles": {
                    "label": {
                        "color": "blue",
                        "backgroundColor": dmc.DEFAULT_THEME["colors"]["yellow"][1],
                    },
                }
            },
            "Input": {
                "styles": {
                    "input": {"borderColor": dmc.DEFAULT_THEME["colors"]["violet"][4]}
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
