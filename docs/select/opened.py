import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.Button("Toggle dropdown", id="btn-select-opened", n_clicks=0),
        dmc.Select(
            label="Select your favorite library",
            placeholder="Select value",
            id="select-opened",
            value="pd",
            data = [
                {"value": "pd", "label": "Pandas"},
                {"value": "np", "label": "NumPy"},
                {"value": "tf", "label": "TensorFlow"},
                {"value": "torch", "label": "PyTorch"},
            ],
            w=400,
            mb=10,
        ),

    ]
)


@callback(
    Output("select-opened", "dropdownOpened"), Input("btn-select-opened", "n_clicks")
)
def select_value(n):
    if n % 2 ==  0:
        return False
    return True
