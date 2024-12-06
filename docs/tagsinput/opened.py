import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.Button("Toggle dropdown", id="btn-tags-opened", n_clicks=0),
        dmc.TagsInput(
            label="Select your favorite library",
            placeholder="Select value",
            id="tags-opened",
            value=["pd"],
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
    Output("tags-opened", "dropdownOpened"), Input("btn-tags-opened", "n_clicks")
)
def select_value(n):
    if n % 2 == 0:
        return False
    return True
