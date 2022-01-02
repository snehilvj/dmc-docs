import random

import dash
from dash import Input, Output, State

from app import app
from reusable_components.component_block import OnlyCodeBlock

data_string = """data = [
        {"value": "react", "label": "React"},
        {"value": "ng", "label": "Angular"},
        {"value": "svelte", "label": "Svelte"},
        {"value": "vue", "label": "Vue"},
    ]"""


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
    Output("checkbox-color", "color"),
    Input("color-checkbox-demo", "value"),
)
def color_checkbox_demo(color):
    return color


####### chips #######
@app.callback(
    Output("chips-code-output", "children"),
    Output("chips-demo", "variant"),
    Output("chips-demo", "color"),
    Output("chips-demo", "radius"),
    Output("chips-demo", "size"),
    Output("chips-demo", "multiple"),
    Output("chips-demo", "spacing"),
    Input("variant-chips-demo", "value"),
    Input("color-chips-demo", "value"),
    Input("radius-chips-demo", "value"),
    Input("size-chips-demo", "value"),
    Input("multiple-chips-demo", "checked"),
    Input("spacing-chips-demo", "value"),
)
def children_badge_demo(variant, color, radius, size, multiple, spacing):
    return [
        OnlyCodeBlock(
            code=f"""import dash_mantine_components as dmc

dmc.Chips(
    {data_string}
    color="{color}",
    radius="{radius}",
    size="{size}",
    spacing="{spacing}",
    variant="{variant}",
    multiple={multiple},
)"""
        ),
        variant,
        color,
        radius,
        size,
        multiple,
        spacing,
    ]


@app.callback(
    Output("chips-demo", "value"),
    Input("multiple-chips-demo", "checked"),
)
def multiple_chips_demo(multiple):
    return ["vue", "react"] if multiple else "react"


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
