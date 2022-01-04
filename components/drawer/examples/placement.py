import dash_mantine_components as dmc
from dash import html, Output, Input, State

component = html.Div(
    [
        dmc.Drawer(id="drawer-position"),
        dmc.Group(
            align="center",
            spacing="xl",
            children=[
                dmc.RadioGroup(
                    id="drawer-position-radio",
                    value="left",
                    data=[
                        {"label": "Left (Default)", "value": "left"},
                        {"label": "Top", "value": "top"},
                        {"label": "Right", "value": "right"},
                        {"label": "Bottom", "value": "bottom"},
                    ],
                ),
                dmc.Button("Open Drawer", id="drawer-position-button"),
            ],
        ),
    ]
)


@app.callback(
    Output("drawer-position", "opened"),
    Output("drawer-position", "position"),
    Input("drawer-position-button", "n_clicks"),
    State("drawer-position-radio", "value"),
    prevent_initial_call=True,
)
def toggle_drawer(n_clicks, position):
    return True, position
