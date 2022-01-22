import dash_labs as dl
from dash import Dash, Output, Input, callback_context as ctx
from dash_iconify import DashIconify
import dash_mantine_components as dmc

from lib.appshell import AppShell

app = Dash(__name__, plugins=[dl.plugins.pages])
app.layout = AppShell(dl.plugins.page_container)

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
            "id": button_id + "notified",
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


if __name__ == "__main__":
    app.server.run(debug=True)
