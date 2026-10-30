import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Drag pills to reorder",
    description="Tags can be reordered by dragging pills",
    placeholder="Enter tag",
    value=["first", "second", "third"],
    w=400,
    withPillsReorder=True
)
