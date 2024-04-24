import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Press Enter to submit a tag",
    placeholder="Enter tag",
    splitChars=[",", " ", "|"],
    w=400,
)
