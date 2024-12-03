import dash_mantine_components as dmc

component = dmc.Paper(
    [
        dmc.TagsInput(
            label="Scrollable dropdown",
            data=[f"Option {i}" for i in range(100)],
            placeholder="Pick value",
            maxDropdownHeight=300,
            w=400,
        ),
        dmc.TagsInput(
            label="With native scroll",
            data=[f"Option {i}" for i in range(100)],
            placeholder="Pick value",
            withScrollArea=False,
            styles={"dropdown": {"maxHeight": 200, "overflowY": "auto"}},
            w=400,
            mt="md",
        ),
    ]
)
