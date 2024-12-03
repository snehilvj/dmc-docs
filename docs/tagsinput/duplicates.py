import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Press Enter to submit a tag",
    placeholder="Duplicates are allowed",
    allowDuplicates=True,
    w=400,
)
