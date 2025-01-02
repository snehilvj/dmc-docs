import dash_mantine_components as dmc
from dash import Input, Output, callback

component = dmc.Group([
    dmc.Box([
        dmc.Text(c="blue.5", id="color-index-text"),
        dmc.Button("Button", color="cyan.5", id="color-index-btn")
    ]),
    dmc.Box([
        dmc.Text("index"),
        dmc.Slider(min=0, max=9, step=1, value=3, id="color-index-slider", w=200)
    ])
], justify="space-between")

@callback(
    Output("color-index-text", "children"),
    Output("color-index-text", "c"),
    Output("color-index-btn", "color"),
    Input("color-index-slider", "value")
)
def update(val):
    return f"Text with blue.{val} color", f"blue.{val}", f"blue.{val}"
