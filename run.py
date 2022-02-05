import dash_labs as dl
import dash_mantine_components as dmc
from dash import Dash, Output, Input, callback_context as ctx
from dash_iconify import DashIconify

from lib.appshell import AppShell

app = Dash(
    __name__,
    plugins=[dl.plugins.pages],
    external_scripts=["https://www.googletagmanager.com/gtag/js?id=G-4PJELX1C4W"],
)
app.layout = AppShell(dl.plugins.page_container)
server = app.server

app.clientside_callback(
    """
    function(value) {
        if (value) {
            document.getElementById(value).click()
        }
        return value
    }
    """,
    Output("dummy-container-for-header-select", "children"),
    Input("select-component", "value"),
)

# noinspection PyProtectedMember
app.clientside_callback(
    """
    function(children) {
        return null
    }
    """,
    Output("select-component", "value"),
    Input(dl.plugins.pages._ID_CONTENT, "children"),
)

app.clientside_callback(
    """
    function(checked) {
        return {colorScheme: checked ? "dark" : "light"}
    }
    """,
    Output("theme-demo", "theme"),
    Input("dark-theme-switch", "checked"),
    prevent_initial_call=True,
)


@app.callback(
    Output("home-notifications-container", "children"),
    Input("default-notification", "n_clicks"),
    Input("green-icon-notification", "n_clicks"),
    Input("10-sec-notification", "n_clicks"),
    Input("orange-loading-notification", "n_clicks"),
    prevent_initial_call=True,
)
def notify(nc1, nc2, nc3, nc4):
    if nc1 or nc2 or nc3 or nc4:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        props = {
            "action": "show",
            "id": button_id + "-notified",
        }

        if button_id == "default-notification":
            props["title"] = "Default Notification"
            props["message"] = "Notifications in Dash is awesome!"

        elif button_id == "green-icon-notification":
            props["title"] = "Green Icon"
            props["message"] = "Your work as been saved."
            props["icon"] = [DashIconify(icon="radix-icons:check-circled")]
            props["color"] = "green"

        elif button_id == "10-sec-notification":
            props["title"] = "10 sec timeout"
            props["message"] = "This notification will dismiss itself after 10 secs."
            props["color"] = "violet"
            props["autoClose"] = 10000

        else:
            props["title"] = "Loading data"
            props["message"] = "The app is loading data, please wait."
            props["color"] = "orange"
            props["loading"] = True

        return dmc.Notification(**props)


app.clientside_callback(
    """
    function(variant, color, radius, size, compact, loading, children) {
        return [
            `import dash_mantine_components as dmc

dmc.Button(
    "${children}",
    variant="${variant}",
    color="${window.colorMap[color]}",
    radius="${window.sizeMap[radius]}",
    size="${window.sizeMap[size]}"
    compact=${compact ? "True" : "False"},
    loading=${loading ? "True" : "False"},
)`,
        variant,
        window.colorMap[color],
        window.sizeMap[radius],
        window.sizeMap[size],
        compact,
        loading,
        children
        ];
    }
    """,
    Output("button-code-output", "children"),
    Output("button-demo", "variant"),
    Output("button-demo", "color"),
    Output("button-demo", "radius"),
    Output("button-demo", "size"),
    Output("button-demo", "compact"),
    Output("button-demo", "loading"),
    Output("button-demo", "children"),
    Input("variant-button-demo", "value"),
    Input("color-button-demo", "value"),
    Input("radius-button-demo", "value"),
    Input("size-button-demo", "value"),
    Input("compact-button-demo", "checked"),
    Input("loading-button-demo", "checked"),
    Input("children-button-demo", "value"),
)

app.clientside_callback(
    """
    function(color) {
        return [
            `import dash_mantine_components as dmc

dmc.Checkbox(
    label="Use me as a boolean input",
    checked=True,
    color="${window.colorMap[color]}"
)`,
        window.colorMap[color]
    ];
    }
    """,
    Output("checkbox-code-output", "children"),
    Output("checkbox-color", "color"),
    Input("color-checkbox-demo", "value"),
)

app.clientside_callback(
    """
    function(variant, color, radius, size, multiple, spacing) {
        return [
            `import dash_mantine_components as dmc

dmc.Chips(
    data = [
        {"value": "react", "label": "React"},
        {"value": "ng", "label": "Angular"},
        {"value": "svelte", "label": "Svelte"},
        {"value": "vue", "label": "Vue"},
    ],
    color="${window.colorMap[color]}",
    radius="${window.sizeMap[radius]}",
    size="${window.sizeMap[size]}",
    spacing="${window.sizeMap[spacing]}",
    variant="${variant}",
    multiple=${multiple ? "True" : "False"},
)`,
        variant,
        window.colorMap[color],
        window.sizeMap[radius],
        window.sizeMap[size],
        multiple,
        window.sizeMap[spacing]
        ];
    }
    """,
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


@app.callback(
    Output("chips-demo", "value"),
    Input("multiple-chips-demo", "checked"),
)
def multiple_chips_demo(multiple):
    return ["vue", "react"] if multiple else "react"


app.clientside_callback(
    """
    function(variant, color, size) {
        return [
            `import dash_mantine_components as dmc

dmc.Loader(
    variant="${variant}",
    color="${window.colorMap[color]}",
    size="${window.sizeMap[size]}"
)`,
        variant,
        window.colorMap[color],
        window.sizeMap[size],
        ];
    }
    """,
    Output("loader-code-output", "children"),
    Output("loader-demo", "variant"),
    Output("loader-demo", "color"),
    Output("loader-demo", "size"),
    Input("variant-loader-demo", "value"),
    Input("color-loader-demo", "value"),
    Input("size-loader-demo", "value"),
)


app.clientside_callback(
    """
    function(size, thickness, roundCaps) {
        return [
            `import dash_mantine_components as dmc

dmc.RingProgress(
    size=${size},
    thickness=${thickness},
    roundCaps=${roundCaps ? "True" : "False"},
    sections=[
        {"value": 40, "color": "red"},
        {"value": 15, "color": "yellow"},
        {"value": 15, "color": "violet"},
    ],
)`,
        size,
        thickness,
        roundCaps,
        ];
    }
    """,
    Output("ringprogress-code-output", "children"),
    Output("ringprogress-demo", "size"),
    Output("ringprogress-demo", "thickness"),
    Output("ringprogress-demo", "roundCaps"),
    Input("size-ringprogress-demo", "value"),
    Input("thickness-ringprogress-demo", "value"),
    Input("caps-ringprogress-demo", "checked"),
)


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=False)
