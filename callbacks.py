import random

import dash
from dash import Input, Output
from dash.exceptions import PreventUpdate


data_string = """data = [
        {"value": "react", "label": "React"},
        {"value": "ng", "label": "Angular"},
        {"value": "svelte", "label": "Svelte"},
        {"value": "vue", "label": "Vue"},
    ]"""


####### button #######


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
