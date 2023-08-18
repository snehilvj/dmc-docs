import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.Button("Open Drawer", id="drawer-demo-button"),
        dmc.Drawer(
            title="Drawer Example",
            id="drawer-simple",
            padding="md",
            zIndex=10000,
        ),
    ]
)


@callback(
    Output("drawer-simple", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True
