import dash_mantine_components as dmc
from dash import Output, Input, clientside_callback, dcc, page_container, State

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
            "colors": {
                "myColor": [
                    "#F2FFB6",
                    "#DCF97E",
                    "#C3E35B",
                    "#AAC944",
                    "#98BC20",
                    "#86AC09",
                    "#78A000",
                    "#668B00",
                    "#547200",
                    "#455D00",
                ]
            },
        },
        children=[
            dcc.Location(id="url", refresh="callback-nav"),
            dmc.NotificationProvider(zIndex=2000),
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
                    "breakpoint": "lg",
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
        const box = document.getElementById("ethical-ads-box");
        if (data === "dark") {
            box.classList.add("dark");
        } else {
            box.classList.remove("dark");
        }
        return dash_clientside.no_update
    }
    """,
    Output("ethical-ads-box", "className"),
    Input("m2d-mantine-provider", "forceColorScheme"),
)

clientside_callback(
    """
    function(n_clicks, theme) {        
        dash_clientside.set_props("m2d-mantine-provider", {
            forceColorScheme: theme === "dark" ? "light" : "dark"
        });
        return dash_clientside.no_update
    }
    """,
    Output("m2d-mantine-provider", "forceColorScheme"),
    Input("color-scheme-toggle", "n_clicks"),
    State("m2d-mantine-provider", "forceColorScheme"),
    prevent_initial_call=True,
)
