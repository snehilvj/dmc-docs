import dash_mantine_components as dmc

component = dmc.Stack(
    children=[
        dmc.Textarea(
            label="Autosize with no rows limit",
            placeholder="Autosize with no rows limit",
            w=500,
            autosize=True,
            minRows=2,
        ),
        dmc.Textarea(
            label="Autosize with 4 rows max",
            placeholder="Autosize with 4 rows max",
            w=500,
            autosize=True,
            minRows=2,
            maxRows=4,
        ),
    ],
)
