
from dash import Dash, html, clientside_callback, Input, Output
import dash_mantine_components as dmc


component = html.Div([
        dmc.Group([
            dmc.Button("Show Notification", id="api-show"),
            dmc.Button("Clean", id="api-clean", variant="outline", color="red"),
            dmc.Button("View Store", id="fetch-notification-store", variant="default"),
        ]),
        html.Pre(id="notification-store", style={"whiteSpace": "pre-wrap", "padding": "10px"}),

])

clientside_callback(
    """(n) => {
        if (n > 0) {
            dash_mantine_components.appNotifications.api.show({
                title: "Client-side Notification",
                message: "Triggered from clientside callback",
                color: "blue",
                autoClose: false
            });
        }
        return 0;
    }""",
    Output("api-show", "n_clicks"),
    Input("api-show", "n_clicks"),
    prevent_initial_call=True
)

clientside_callback(
    """() => {
        dash_mantine_components.appNotifications.api.clean()
        return null;
    }""",
    Output("api-clean", "n_clicks"),
    Input("api-clean", "n_clicks"),
    prevent_initial_call=True
)

clientside_callback(
    """() => {
        return JSON.stringify(dash_mantine_components.appNotifications.store, null, 2)
    }""",
    Output("notification-store", "children"),
    Input("fetch-notification-store", "n_clicks"),
    prevent_initial_call=True
)
