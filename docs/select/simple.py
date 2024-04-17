import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.Select(
            label="Select framework",
            placeholder="Select one",
            id="framework-select",
            value="ng",
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            w=200,
            mb=10,
        ),
        dmc.Text(id="selected-value"),
    ]
)


@callback(Output("selected-value", "children"), Input("framework-select", "value"))
def select_value(value):
    return value
