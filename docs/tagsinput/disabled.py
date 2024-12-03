import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Disabled",
    disabled=True,
    value=["First", "Second"],
    w=400,
)
