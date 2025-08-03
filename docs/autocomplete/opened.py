import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.Button("Toggle dropdown", id="btn-autocomplete-opened", n_clicks=0),
        dmc.Autocomplete(
            label="Select your favorite library",
            placeholder="Select value",
            id="autocomplete-opened",
            data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
            comboboxProps={"position": "bottom", "middlewares": {"flip": False, "shift": False}},
            w=400,
            mb=10,
        ),
    ]
)


@callback(
    Output("autocomplete-opened", "dropdownOpened"), Input("btn-autocomplete-opened", "n_clicks")
)
def select_value(n):
    if n % 2 == 0:
        return False
    return True
