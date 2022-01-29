import dash_mantine_components as dmc
from dash import Output, Input, html
from dash import callback  # no-prism

component = html.Div(
    [
        dmc.MultiSelect(
            label="Select frameworks",
            placeholder="Select all you like!",
            id="framework-multi-select",
            value=["ng", "vue"],
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            style={"width": 400},
        ),
        dmc.Space(h=10),  # no-prism
        dmc.Text(id="multi-selected-value"),
    ]
)


@callback(
    Output("multi-selected-value", "children"), Input("framework-multi-select", "value")
)
def select_value(value):
    return ", ".join(value)
