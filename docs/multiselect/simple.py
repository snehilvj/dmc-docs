import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.MultiSelect(
            label="Select your favorite libraries",
            placeholder="Select all you like!",
            id="framework-multi-select",
            value=["pd", "torch"],
            data=[
                {"value": "pd", "label": "Pandas"},
                {"value": "np", "label": "NumPy"},
                {"value": "tf", "label": "TensorFlow"},
                {"value": "torch", "label": "PyTorch"},
            ],
            w=400,
            mb=10,
        ),
        dmc.Text(id="multi-selected-value"),
    ]
)


@callback(
    Output("multi-selected-value", "children"), Input("framework-multi-select", "value")
)
def select_value(value):
    return ", ".join(value)
