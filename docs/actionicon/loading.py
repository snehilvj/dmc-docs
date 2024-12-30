import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import callback, Input, Output

component = dmc.Box([
    dmc.Group(
        [
            dmc.ActionIcon(
                id="icon-loading-default",
                children=DashIconify(icon="tabler:heart", width=18, height=18)
            ),
            dmc.ActionIcon(
                id="icon-loading-light",
                children=DashIconify(icon="tabler:heart", width=18, height=18),
                variant="light",
            ),
            dmc.ActionIcon(
                id="icon-loading-outline",
                children=DashIconify(icon="tabler:heart", width=18, height=18),
                variant="outline",
            ),
        ]
    ),
    dmc.Switch(
        id="loading-switch",
        label="Loading state",
        checked=False,
        mt="md",
    ),
])


@callback(
    Output("icon-loading-default", "loading"),
    Output("icon-loading-light", "loading"),
    Output("icon-loading-outline", "loading"),
    Input("loading-switch", "checked"),
)
def toggle_loading(loading_state):
    return loading_state, loading_state, loading_state

