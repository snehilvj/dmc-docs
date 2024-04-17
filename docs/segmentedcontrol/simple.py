import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.SegmentedControl(
            id="segmented",
            value="ng",
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            mb=10,
        ),
        dmc.Text(id="segmented-value"),
    ]
)


@callback(Output("segmented-value", "children"), Input("segmented", "value"))
def select_value(value):
    return value
