import random

import dash
from dash import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app


####### alert #######
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


####### badge #######
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


####### button #######
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


####### checkbox #######
@app.callback(
    Output("checkbox-demo", "color"),
    Input("color-checkbox-demo", "value"),
)
def color_checkbox_demo(color):
    return color


@app.callback(
    Output("checkbox-demo", "size"),
    Input("size-checkbox-demo", "value"),
)
def size_checkbox_demo(size):
    return size


@app.callback(
    Output("checkbox-demo", "label"),
    Input("label-checkbox-demo", "value"),
)
def label_checkbox_demo(label):
    return label


####### chips #######
@app.callback(
    Output("chips-demo", "variant"),
    Input("variant-chips-demo", "value"),
)
def variant_chips_demo(variant):
    return variant


@app.callback(
    Output("chips-demo", "color"),
    Input("color-chips-demo", "value"),
)
def color_chips_demo(color):
    return color


@app.callback(
    Output("chips-demo", "radius"),
    Input("radius-chips-demo", "value"),
)
def radius_chips_demo(radius):
    return radius


@app.callback(
    Output("chips-demo", "size"),
    Input("size-chips-demo", "value"),
)
def size_chips_demo(size):
    return size


@app.callback(
    Output("chips-demo", "spacing"),
    Input("spacing-chips-demo", "value"),
)
def spacing_chips_demo(spacing):
    return spacing


@app.callback(
    Output("chips-demo", "multiple"),
    Output("chips-demo", "value"),
    Input("multiple-chips-demo", "checked"),
)
def multiple_chips_demo(multiple):
    if multiple:
        return multiple, ["vue", "react"]
    return multiple, "react"


####### datepicker #######
@app.callback(
    Output("datepicker-demo", "dropdownType"),
    Input("dropdown-datepicker-demo", "value"),
)
def dropdown_datepicker_demo(dropdown):
    return dropdown


@app.callback(
    Output("datepicker-demo", "format"),
    Input("format-datepicker-demo", "value"),
)
def format_datepicker_demo(format):
    return format


@app.callback(
    Output("datepicker-demo", "amountOfMonths"),
    Input("amount-datepicker-demo", "value"),
)
def amount_datepicker_demo(amount):
    if amount:
        return int(amount)
    else:
        raise PreventUpdate


@app.callback(
    Output("datepicker-demo", "initialLevel"),
    Input("initial-datepicker-demo", "value"),
)
def initial_datepicker_demo(initial):
    return initial


####### daterangepicker #######
@app.callback(
    Output("daterangepicker-demo", "dropdownType"),
    Input("dropdown-daterangepicker-demo", "value"),
)
def dropdown_daterangepicker_demo(dropdown):
    return dropdown


@app.callback(
    Output("daterangepicker-demo", "format"),
    Input("format-daterangepicker-demo", "value"),
)
def format_daterangepicker_demo(format):
    return format


@app.callback(
    Output("daterangepicker-demo", "amountOfMonths"),
    Input("amount-daterangepicker-demo", "value"),
)
def amount_daterangepicker_demo(amount):
    if amount:
        return int(amount)
    else:
        raise PreventUpdate


@app.callback(
    Output("daterangepicker-demo", "initialLevel"),
    Input("initial-daterangepicker-demo", "value"),
)
def initial_daterangepicker_demo(initial):
    return initial


####### drawer #######
@app.callback(
    Output("drawer-demo", "opened"),
    Output("drawer-demo", "position"),
    Output("drawer-demo", "size"),
    Output("drawer-demo", "title"),
    Output("drawer-demo", "noOverlay"),
    Input("drawer-demo-button", "n_clicks"),
    State("position-drawer-demo", "value"),
    State("size-drawer-demo", "value"),
    State("title-drawer-demo", "value"),
    State("overlay-drawer-demo", "checked"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks, position, size, title, noOverlay):
    return True, position, size, title, noOverlay


####### modal #######
@app.callback(
    Output("modal-demo", "opened"),
    Output("modal-demo", "centered"),
    Input("modal-demo-button", "n_clicks"),
    Input("modal-close-button", "n_clicks"),
    Input("modal-submit-button", "n_clicks"),
    State("modal-demo", "opened"),
    State("centered-modal-demo", "checked"),
    prevent_initial_call=True,
)
def modal_demo(nc1, nc2, nc3, opened, centered):
    return not opened, centered


@app.callback(
    Output("modal-size-demo", "opened"),
    Output("modal-size-demo", "size"),
    Input("lg-button-modal", "n_clicks"),
    Input("378px-button-modal", "n_clicks"),
    Input(r"55%-button-modal", "n_clicks"),
    Input("full-button-modal", "n_clicks"),
    prevent_initial_call=True,
)
def modal_size_demo(nc0, nc1, nc2, nc3):
    ctx = dash.callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        return True, button_id.split("-")[0]
    raise PreventUpdate


####### notifications #######
@app.callback(
    Output("notifications-demo-handler", "task"),
    Input("show-notifications-demo", "n_clicks"),
    Input("update-notifications-demo", "n_clicks"),
    Input("hide-notifications-demo", "n_clicks"),
    prevent_initial_call=True,
)
def notifications(show_click, update_click, hide_click):
    command = dash.callback_context.triggered[0]["prop_id"].split("-")[0]
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
