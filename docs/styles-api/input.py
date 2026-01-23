import dash_mantine_components as dmc

component = dmc.TextInput(
    label="TextInput with custom styles",
    placeholder="TextInput with custom styles",
    description="Description below the input",
    w=300,
    styles={
        "input": {"borderColor":  "var(--mantine-color-violet-4)"},
        "label": {
            "color": "blue",
            "backgroundColor":  "var(--mantine-color-yellow-1)",
        },
    },
)
