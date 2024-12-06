import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Read only",
    placeholder="Enter tag",
    readOnly=True,
    value=["First", "Second"],
    w=400,
)
