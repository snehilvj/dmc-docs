import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.Button("Open Drawer", id="drawer-transition-button"),
        dmc.Drawer(
            title="Drawer Example",
            id="drawer-fancy",
            padding="md",
            transitionProps={
                "transition": "rotate-left",
                "duration": 1000,
                "timingFunction": "ease",
            },
            zIndex=10000,
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
