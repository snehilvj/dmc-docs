import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.Button("Open Drawer", id="drawer-transition-button"),
        dmc.Drawer(
            title="Drawer Example",
            id="drawer-fancy",
            padding="md",
            transition="rotate-left",
            transitionDuration=250,
            transitionTimingFunction="ease",
        ),
    ]
)


@callback(
    Output("drawer-fancy", "opened"),
    Input("drawer-transition-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True
