import dash_mantine_components as dmc
from dash import callback, Input, Output

component = dmc.Box(
    [
        dmc.Group(
            dmc.ChipGroup(
                [
                    dmc.Chip("Multiple chips", value="a"),
                    dmc.Chip("Can be selected", value="b"),
                    dmc.Chip("At a time", value="c"),
                ],
                multiple=True,
                value=["a", "b"],
                id="chipgroup-multi",
            ),
            justify="center",
        ),
        dmc.Text(id="chipgroup-multi-container", ta="center"),
    ]
)


@callback(
    Output("chipgroup-multi-container", "children"), Input("chipgroup-multi", "value")
)
def checkbox(value):
    return f"Selected chips: {value}"
