import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.ChipGroup(
            dmc.Group(
                [
                    dmc.Chip(x, value=x, variant="outline")
                    for x in ["React", "Django", "Dash", "Vue"]
                ],
                my=10,
            ),
            id="chips-callback",
            value=["React"],
            multiple=True,
            mb=10,
        ),
        dmc.Text(id="chips-values-output"),
    ]
)


@callback(
    Output("chips-values-output", "children"),
    Input("chips-callback", "value"),
)
def chips_values(value):
    return ", ".join(value) if value else None
