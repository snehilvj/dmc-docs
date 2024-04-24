import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Select frameworks",
    description="You can select a maximum of 3 frameworks.",
    maxTags=3,
    w=400,
)
