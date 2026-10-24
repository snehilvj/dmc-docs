import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Custom pills",
    description="Tags are rendered with a star prefix",
    placeholder="Enter tag",
    value=["React", "Angular"],
    renderPill={"function": "renderTagPill"}
)