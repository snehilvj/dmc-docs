import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.Select(
            label="Select your favorite library",
            placeholder="Select one",
            id="framework-select",
            value="pd",
            data=[
                {"value": "pd", "label": "Pandas"},
                {"value": "np", "label": "NumPy"},
                {"value": "tf", "label": "TensorFlow"},
                {"value": "torch", "label": "PyTorch"},
            ],
            w=200,
            mb=10,
        ),
        dmc.Text(id="selected-value"),
    ]
)


@callback(Output("selected-value", "children"), Input("framework-select", "value"))
def select_value(value):
    return f" You selected {value}"
