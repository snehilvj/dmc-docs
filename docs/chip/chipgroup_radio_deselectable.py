import dash_mantine_components as dmc
from dash import callback, Input, Output

component = dmc.Box(
    [
        dmc.Group(
            dmc.ChipGroup(
                [
                    dmc.Chip("Single chip", value="a"),
                    dmc.Chip("Can be selected", value="b"),
                    dmc.Chip("At a time", value="c"),
                ],
                multiple=False,
                value="a",
                deselectable=True,
                id="chipgroup-deselect",
            ),
            justify="center",
        ),
        dmc.Text(id="chipgroup-deselect-container", ta="center"),
    ]
)


@callback(
    Output("chipgroup-deselect-container", "children"), Input("chipgroup-deselect", "value")
)
def checkbox(value):
    return f"You selected chip: {value}"
