import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.TagsInput(
            label="Boolean error",
            placeholder="Boolean error",
            error=True,
            value=["React", "Angular"],
        ),
        dmc.TagsInput(
            label="With error message",
            placeholder="With error message",
            error="Invalid name",
            value=["React", "Angular"],
        ),
    ]
)