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
                id="chipgroup-single",
            ),
            justify="center",
        ),
        dmc.Text(id="chipgroup-single-container", ta="center"),
    ]
)


@callback(
    Output("chipgroup-single-container", "children"), Input("chipgroup-single", "value")
)
def checkbox(value):
    return f"You selected chip: {value}"
