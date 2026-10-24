from dash import callback, Input, Output
import dash_mantine_components as dmc

component = dmc.Box([
    dmc.Button("Toggle Content", id="collapse-horizontal-btn", n_clicks=0),
    dmc.Collapse(
        children=dmc.Text("Hello World!", my="lg", w=200, bg="blue.3", c="white", p="lg"),
        orientation="horizontal",
        opened=False,
        id="collapse-horizontal"
    )
])

@callback(
    Output("collapse-horizontal", "opened"),
    Input("collapse-horizontal-btn", "n_clicks"),
)
def update(n):
    if n % 2 == 0:
        return False
    return True
