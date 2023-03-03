import dash_mantine_components as dmc
from dash import callback, html, Input, Output

initial_values = [
    [
        {"value": "react", "label": "React"},
        {"value": "ng", "label": "Angular"},
        {"value": "next", "label": "Next.js"},
        {"value": "blitz", "label": "Blitz.js"},
        {"value": "gatsby", "label": "Gatsby.js"},
        {"value": "vue", "label": "Vue"},
        {"value": "jq", "label": "jQuery"},
    ],
    [
        {"value": "sv", "label": "Svelte"},
        {"value": "rw", "label": "Redwood"},
        {"value": "np", "label": "NumPy"},
        {"value": "dj", "label": "Django"},
        {"value": "fl", "label": "Flask"},
    ],
]

component = html.Div([
    dmc.TransferList(id="transfer-list-simple", value=initial_values),
    dmc.Text(id="transfer-list-values-1", mt=20),
    dmc.Text(id="transfer-list-values-2", mt=20)
])


@callback(
    Output("transfer-list-values-1", "children"),
    Output("transfer-list-values-2", "children"),
    Input("transfer-list-simple", "value"),
)
def print_values(value):
    res1 = "List 1: " + ", ".join([item["value"] for item in value[0]])
    res2 = "List 2: " + ", ".join([item["value"] for item in value[1]])
    return res1, res2
