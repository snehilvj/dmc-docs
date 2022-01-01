import random

import dash
from dash import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from reusable_components.component_block import OnlyCodeBlock


####### badge #######
@app.callback(
    Output("badge-code-output", "children"),
    Output("badge-demo", "variant"),
    Output("badge-demo", "color"),
    Output("badge-demo", "radius"),
    Output("badge-demo", "size"),
    Output("badge-demo", "children"),
    Input("variant-badge-demo", "value"),
    Input("color-badge-demo", "value"),
    Input("radius-badge-demo", "value"),
    Input("size-badge-demo", "value"),
    Input("children-badge-demo", "value"),
)
def children_badge_demo(variant, color, radius, size, children):
    return [
        OnlyCodeBlock(
            code=f"""import dash_mantine_components as dmc

dmc.Badge(
    "{children}",
    variant="{variant}",
    color="{color}",
    radius="{radius}",
    size="{size}"
)"""
        ),
        variant,
        color,
        radius,
        size,
        children,
    ]


####### button #######
@app.callback(
    Output("button-code-output", "children"),
    Output("button-demo", "variant"),
    Output("button-demo", "color"),
    Output("button-demo", "radius"),
    Output("button-demo", "size"),
    Output("button-demo", "loading"),
    Output("button-demo", "compact"),
    Output("button-demo", "children"),
    Input("variant-button-demo", "value"),
    Input("color-button-demo", "value"),
    Input("radius-button-demo", "value"),
    Input("size-button-demo", "value"),
    Input("loading-button-demo", "checked"),
    Input("compact-button-demo", "checked"),
    Input("children-button-demo", "value"),
)
def children_badge_demo(variant, color, radius, size, loading, compact, children):
    return [
        OnlyCodeBlock(
            code=f"""import dash_mantine_components as dmc

dmc.Button(
    "{children}",
    variant="filled",
    color="{color}",
    radius="{radius}",
    size="{size}",
    loading={loading},
    compact={compact},
)"""
        ),
        variant,
        color,
        radius,
        size,
        loading,
        compact,
        children,
    ]


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