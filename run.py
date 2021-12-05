import dash
from dash import Dash, html, Output, Input, State
from datetime import datetime
import dash_mantine_components as dmc
from utils import create_component_title
from components.accordion import accordion
from components.affix import affix
from components.alert import alert
from components.badge import badge
from components.button import button
from components.checkbox import checkbox
from components.chips import chips
from components.datepicker import datepicker
from components.divider import divider
from components.drawer import drawer
from components.image import image
from components.modal import modal
from components.notifications import notifications
from components.header import header

app = Dash(__name__)


app.layout = dmc.Container(
    style={"padding": 20},
    children=[
        header,
        dmc.Space(h=30),
        accordion,
        affix,
        alert,
        badge,
        button,
        checkbox,
        chips,
        datepicker,
        divider,
        drawer,
        image,
        modal,
        notifications,
    ],
)


# callbacks
@app.callback(
    Output("alert", "show"),
    Input("alert-button", "n_clicks"),
    State("alert", "show"),
    prevent_initial_call=True,
)
def restart(n_clicks, show):
    return not show


@app.callback(
    Output("drawer", "opened"),
    Input("drawer-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer(n_clicks):
    return True


@app.callback(
    Output("modal", "opened"),
    Input("modal-button", "n_clicks"),
    Input("modal-close-button", "n_clicks"),
    Input("modal-submit-button", "n_clicks"),
    State("modal", "opened"),
    prevent_initial_call=True,
)
def modal(nc1, nc2, nc3, opened):
    return not opened


@app.callback(
    Output("handler", "task"),
    Input("show", "n_clicks"),
    Input("update", "n_clicks"),
    Input("hide", "n_clicks"),
    prevent_initial_call=True,
)
def notifications(show_click, update_click, hide_click):
    command = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
    task = {
        "command": command,
        "id": "notification",
    }
    if command == "show":
        task = {
            **task,
            "props": {
                "color": "violet",
                "title": "This is a notification",
                "message": "Notifications in Dash Apps! Great!",
                "loading": True,
                "disallowClose": True,
                "autoClose": 8000,
            },
        }
    elif command == "update":
        task = {
            **task,
            "props": {
                "color": "green",
                "title": "All good",
                "message": "Data has been loaded.",
                "loading": False,
                "disallowClose": False,
                "autoClose": 3000,
            },
        }

    return task


if __name__ == "__main__":
    app.run_server(debug=True)
