from dash import callback, Input, Output
import dash_mantine_components as dmc

component = dmc.Box([
    dmc.Button("Toggle Content", id="collapse-transition-btn", n_clicks=0),
    dmc.Collapse(
        children=dmc.Text("Hello World!", my="lg"),
        opened=False,
        transitionDuration=1000,
        transitionTimingFunction="linear",
        id="collapse-transition"
    )
])

@callback(
    Output("collapse-transition", "opened"),
    Input("collapse-transition-btn", "n_clicks"),
)
def update(n):
    if n % 2 == 0:
        return False
    return True
