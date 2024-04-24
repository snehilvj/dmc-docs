import dash_mantine_components as dmc

component = dmc.TagsInput(
    w=400,
    label="Press Enter to submit a tag",
    placeholder="Pick tag from list",
    data=["React", "Angular", "Svelte"],
)
