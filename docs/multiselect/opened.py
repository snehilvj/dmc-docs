import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.Button("Toggle dropdown", id="btn-multi-select-opened", n_clicks=0),
        dmc.MultiSelect(
            label="Select your favorite libraries",
            placeholder="Select all you like!",
            id="multi-select-opened",
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
    ]
)


@callback(
    Output("multi-select-opened", "dropdownOpened"),
    Input("btn-multi-select-opened", "n_clicks"),
)
def select_value(n):
    if n % 2 == 0:
        return False
    return True
