import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.Autocomplete(
            label="Select your favorite library",
            placeholder="Pick value or enter anything",
            id="framework-autocomplete",
            data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
            w=200,
            mb=10,
        ),
        dmc.Text(id="autocomplete-value"),
    ]
)


@callback(Output("autocomplete-value", "children"), Input("framework-autocomplete", "value"))
def select_value(value):
    return f" You selected {value}"
