import dash_mantine_components as dmc

component = dmc.Stack([
    dmc.DatePickerInput(
        label="Default Calendar style"
    ),
    dmc.DatePickerInput(
        label="Calendar without red weekend days",
        styles={"day": {"color": "var(--mantine-color-text)"}},
    )
])
