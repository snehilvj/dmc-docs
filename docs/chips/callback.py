import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.Chips(
            id="chips-values",
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            value="react",
        ),
        dmc.Space(h=10),
        dmc.Text(id="chips-values-output"),
    ]
)


@callback(
    Output("chips-values-output", "children"),
    Input("chips-values", "value"),
)
def chips_values(value):
    return value
