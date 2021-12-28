from dash import Input, Output, State
import random
from app import app


@app.callback(
    Output("alert-demo", "color"),
    Input("color-alert-demo", "value"),
)
def color_alert_demo(color):
    return color


@app.callback(
    Output("alert-demo", "children"),
    Input("children-alert-demo", "value"),
)
def children_alert_demo(children):
    return children


@app.callback(
    Output("alert-demo", "title"),
    Input("title-alert-demo", "value"),
)
def title_alert_demo(title):
    return title


@app.callback(
    Output("alert-demo", "withCloseButton"),
    Input("close-alert-demo", "checked"),
)
def close_alert_demo(withCloseButton):
    return withCloseButton


@app.callback(
    Output("alert", "show"),
    Input("alert-button", "n_clicks"),
    State("alert", "show"),
    prevent_initial_call=True,
)
def alert(n_clicks, show):
    return not show


@app.callback(
    Output("badge-demo", "variant"),
    Input("variant-badge-demo", "value"),
)
def variant_badge_demo(variant):
    return variant


@app.callback(
    Output("badge-demo", "color"),
    Input("color-badge-demo", "value"),
)
def color_badge_demo(color):
    return color


@app.callback(
    Output("badge-demo", "radius"),
    Input("radius-badge-demo", "value"),
)
def radius_badge_demo(radius):
    return radius


@app.callback(
    Output("badge-demo", "size"),
    Input("size-badge-demo", "value"),
)
def size_badge_demo(size):
    return size


@app.callback(
    Output("badge-demo", "children"),
    Input("children-badge-demo", "value"),
)
def children_badge_demo(children):
    return children


@app.callback(
    Output("button-demo", "variant"),
    Input("variant-button-demo", "value"),
)
def variant_button_demo(variant):
    return variant


@app.callback(
    Output("button-demo", "color"),
    Input("color-button-demo", "value"),
)
def color_button_demo(color):
    return color


@app.callback(
    Output("button-demo", "radius"),
    Input("radius-button-demo", "value"),
)
def radius_button_demo(radius):
    return radius


@app.callback(
    Output("button-demo", "size"),
    Input("size-button-demo", "value"),
)
def size_button_demo(size):
    return size


@app.callback(
    Output("button-demo", "loading"),
    Input("loading-button-demo", "checked"),
)
def loading_button_demo(loading):
    return loading


@app.callback(
    Output("button-demo", "compact"),
    Input("compact-button-demo", "checked"),
)
def compact_button_demo(compact):
    return compact


@app.callback(
    Output("button-demo", "children"),
    Input("children-button-demo", "value"),
)
def children_button_demo(children):
    return children


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


@app.callback(Output("progress", "value"), Input("progress-button", "n_clicks"))
def progress(n_clicks):
    return random.randint(1, 100)


@app.callback(
    Output("slider-output", "children"),
    Input("slider", "value"),
    prevent_initial_call=True,
)
def slider(value):
    return f"Slider value: {value}"


@app.callback(
    Output("slider-drag-output", "children"),
    Input("slider", "drag_value"),
    prevent_initial_call=True,
)
def slider_drag(value):
    return f"Slider drag value: {value}"
