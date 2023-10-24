import dash_mantine_components as dmc
from dash import (
    Output,
    Input,
    clientside_callback,
    html,
    dcc,
    page_container,
    State,
)

from components.header import create_header
from components.sidebar import create_navbar_drawer, create_side_navbar
from lib.constants import PRIMARY_COLOR


def create_appshell(data):
    return dmc.MantineProvider(
        dmc.MantineProvider(
            theme={
                "fontFamily": "'Inter', sans-serif",
                "primaryColor": PRIMARY_COLOR,
                "components": {
                    "Button": {"styles": {"root": {"fontWeight": 400}}},
                    "Alert": {"styles": {"title": {"fontWeight": 500}}},
                    "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                    "Badge": {"styles": {"root": {"fontWeight": 500}}},
                    "Progress": {"styles": {"label": {"fontWeight": 500}}},
                    "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
                    "Table": {
                        "defaultProps": {
                            "highlightOnHover": True,
                            "withBorder": True,
                            "verticalSpacing": "sm",
                            "horizontalSpacing": "md",
                        }
                    },
                },
            },
            inherit=True,
            children=[
                dcc.Store(id="theme-store", storage_type="local"),
                dcc.Location(id="url", refresh="callback-nav"),
                dmc.Notifications(),
                create_header(data),
                create_side_navbar(data),
                create_navbar_drawer(data),
                html.Div(
                    dmc.Container(size="lg", pt=90, children=page_container),
                    id="wrapper",
                ),
            ],
        ),
        theme={"colorScheme": "light"},
        id="mantine-docs-theme-provider",
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )


clientside_callback(
    """
    function(data) {
        return data
    }
    """,
    Output("mantine-docs-theme-provider", "theme"),
    Input("theme-store", "data"),
)

clientside_callback(
    """
    function(n_clicks, data) {
        if (data) {
            if (n_clicks) {
                const scheme = data["colorScheme"] == "dark" ? "light" : "dark"
                return { colorScheme: scheme } 
            }
            return dash_clientside.no_update
        } else {
            return { colorScheme: "light" }
        }
    }
    """,
    Output("theme-store", "data"),
    Input("color-scheme-toggle", "n_clicks"),
    State("theme-store", "data"),
)
