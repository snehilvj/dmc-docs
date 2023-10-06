import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback

component = html.Div(
    [
        dmc.Drawer(
            title="Size: md", id="drawer-size-md", padding="md", size="md", zIndex=10000
        ),
        dmc.Drawer(
            title="Size: 450px",
            id="drawer-size-450",
            padding="md",
            size=450,
            zIndex=10000,
        ),
        dmc.Drawer(
            title="Size: 55%",
            id="drawer-size-55",
            padding="md",
            size="55%",
            zIndex=10000,
        ),
        dmc.Drawer(
            title="Size: full",
            id="drawer-size-full",
            padding="md",
            size="100%",
            zIndex=10000,
        ),
        dmc.Group(
            [
                dmc.Button("md", id="md-drawer-button"),
                dmc.Button("450px", id="450-drawer-button"),
                dmc.Button("55%", id="55-drawer-button"),
                dmc.Button("full", id="full-drawer-button"),
            ]
        ),
    ]
)


def toggle_drawer(n_clicks, opened):
    return not opened


for size in ["md", "450", "55", "full"]:
    callback(
        Output(f"drawer-size-{size}", "opened"),
        Input(f"{size}-drawer-button", "n_clicks"),
        State(f"drawer-size-{size}", "opened"),
        prevent_initial_call=True,
    )(toggle_drawer)
