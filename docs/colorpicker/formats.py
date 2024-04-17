import dash_mantine_components as dmc
from dash import html, Input, Output, callback

component = html.Div(
    [
        dmc.Group(
            justify="space-between",
            children=[
                dmc.ColorPicker(id="colorpicker-format", format="hex", value="#343353"),
                dmc.Select(
                    id="format-select",
                    data=[
                        {"label": fmt.upper(), "value": fmt}
                        for fmt in ["hex", "hexa", "rgb", "rgba", "hsl", "hsla"]
                    ],
                    value="hex",
                ),
            ],
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-color-format"),
    ]
)


@callback(Output("colorpicker-format", "format"), Input("format-select", "value"))
def pick_format(value):
    return value


@callback(
    Output("selected-color-format", "children"), Input("colorpicker-format", "value")
)
def pick_color(color):
    return color
