from dash import callback, Input, Output
import dash_mantine_components as dmc

component = dmc.Box([
    dmc.Button("Toggle Content", id="collapse-btn", n_clicks=0),
    dmc.Collapse(
        children=dmc.Text("Hello World!", my="lg"),
        opened=False,
        id="collapse-simple"
    )
])

@callback(
    Output("collapse-simple", "opened"),
    Input("collapse-btn", "n_clicks"),
)
def update(n):
    print(n)
    if n % 2 == 0:
        return False
    return True
