import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.TextInput(
            id="persisted-input",
            label="With persistence",
            placeholder="This will stick",
            persistence=True,
        ),
        dmc.TextInput(
            id="non-persisted-input",
            label="Without persistence",
            placeholder="This will reset",
        ),
    ],
)