import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback

data = [
    ["Left (Default)", "left"],
    ["Top", "top"],
    ["Right", "right"],
    ["Bottom", "bottom"],
]

component = html.Div(
    [
        dmc.Drawer(
            id="drawer-position",
            zIndex=10000,
        ),
        dmc.Group(
            align="center",
            spacing="xl",
            children=[
                dmc.RadioGroup(
                    [dmc.Radio(label, value=value) for label, value in data],
                    id="drawer-position-radio",
                    value="left",
                ),
                dmc.Button("Open Drawer", id="drawer-position-button"),
            ],
        ),
    ]
)


@callback(
    Output("drawer-position", "opened"),
    Output("drawer-position", "position"),
    Input("drawer-position-button", "n_clicks"),
    State("drawer-position-radio", "value"),
    prevent_initial_call=True,
)
def toggle_drawer(n_clicks, position):
    return True, position
