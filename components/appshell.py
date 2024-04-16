import dash_mantine_components as dmc
from dash import Output, Input, clientside_callback, html, dcc, page_container, State

from components.header import create_header
from components.navbar import create_navbar, create_navbar_drawer
from lib.constants import PRIMARY_COLOR


def create_appshell(data):
    return dmc.MantineProvider(
        id="m2d-mantine-provider",
        forceColorScheme="light",
        theme={
            "primaryColor": PRIMARY_COLOR,
            "fontFamily": "'Inter', sans-serif",
            "components": {
                "Button": {"defaultProps": {"fw": 400}},
                "Alert": {"styles": {"title": {"fontWeight": 500}}},
                "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                "Badge": {"styles": {"root": {"fontWeight": 500}}},
                "Progress": {"styles": {"label": {"fontWeight": 500}}},
                "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
                "CodeHighlightTabs": {"styles": {"file": {"padding": 12}}},
                "Table": {
                    "defaultProps": {
                        "highlightOnHover": True,
                        "withTableBorder": True,
                        "verticalSpacing": "sm",
                        "horizontalSpacing": "md",
                    }
                },
            },
        },
        children=[
            dcc.Store(id="theme-store", storage_type="local", data="light"),
            dcc.Location(id="url", refresh="callback-nav"),
            dmc.NotificationProvider(),
            dmc.AppShell(
                [
                    create_header(data),
                    create_navbar(data),
                    create_navbar_drawer(data),
                    dmc.AppShellMain(children=page_container),
                ],
                header={"height": 70},
                padding="xl",
                zIndex=1400,
                navbar={
                    "width": 300,
                    "breakpoint": "sm",
                    "collapsed": {"mobile": True},
                },
                aside={
                    "width": 300,
                    "breakpoint": "xl",
                    "collapsed": {"desktop": False, "mobile": True},
                },
            ),
        ],
    )


clientside_callback(
    """
    function(data) {
        return data
    }
    """,
    Output("m2d-mantine-provider", "forceColorScheme"),
    Input("theme-store", "data"),
)

clientside_callback(
    """
    function(data) {
        const element = document.getElementById("ethical-ads-box")
        if (data === "dark") {
            element.className += " dark"
        } else {
            element.className = element.className.replace(" dark", "")
        }
        return dash_clientside.no_update
    }
    """,
    Output("ethical-ads-box", "className"),
    Input("theme-store", "data"),
)

clientside_callback(
    """
    function(n_clicks, data) {
        return data === "dark" ? "light" : "dark";
    }
    """,
    Output("theme-store", "data"),
    Input("color-scheme-toggle", "n_clicks"),
    State("theme-store", "data"),
    prevent_initial_call=True,
)
