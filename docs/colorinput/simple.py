import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.ColorInput(id="color-input", label="Your favorite color"),
        dmc.Space(h=10),
        dmc.Text(id="selected-color-input"),
    ]
)


@callback(Output("selected-color-input", "children"), Input("color-input", "value"))
def pick(color):
    return f"You selected: {color}"
