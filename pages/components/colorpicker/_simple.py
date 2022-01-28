import dash_mantine_components as dmc
from dash import Output, Input, html
from dash import callback  # no-prism

component = html.Div(
    [
        dmc.ColorPicker(id="colorpicker", format="rgba", value="rgba(41, 96, 214, 1)"),
        dmc.Space(h=20),  # no-prism
        dmc.Text(id="selected-color"),
    ]
)


@callback(Output("selected-color", "children"), Input("colorpicker", "value"))
def pick(color):
    return color
