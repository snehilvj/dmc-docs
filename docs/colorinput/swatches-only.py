import dash_mantine_components as dmc

component = dmc.ColorInput(
    label="Your favorite color",
    value="#40c057",
    disallowInput=True,
    withPicker=False,
    swatches = dmc.theme.DEFAULT_COLORS["red"] + dmc.theme.DEFAULT_COLORS["green"]
)

