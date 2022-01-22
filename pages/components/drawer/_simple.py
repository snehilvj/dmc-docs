import dash_mantine_components as dmc
from dash import callback  # no-prism
from dash import html, Output, Input

component = html.Div(
    [
        dmc.Button("Open Drawer", id="drawer-demo-button"),
        dmc.Drawer(
            title="Drawer Example",
            id="drawer",
            padding="md",
        ),
    ]
)


@callback(
    Output("drawer", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True
