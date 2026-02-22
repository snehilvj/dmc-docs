import dash_mantine_components as dmc
from dash import  Output, Input, State, callback, clientside_callback, dcc, page_container, no_update
from dash_iconify import DashIconify

from components.header import create_header
from components.navbar import create_navbar, create_navbar_drawer
from lib.constants import PRIMARY_COLOR


def create_appshell(data):
    return dmc.DirectionProvider(dmc.MantineProvider(
        id="m2d-mantine-provider",
        theme={
            "primaryColor": PRIMARY_COLOR,
            "fontFamily": "'Inter', sans-serif",
            "breakpoints": {
                "sm": "43em",
                "lg": "67.5em",  #allows navbar to be visible on an ipad
                "xl":"78em",    #toc breakpoint (matches Mantine's)
                "xxl": "100em",
            },
            "components": {
                "Button": {"defaultProps": {"fw": 400}},
                "Blockquote": {"styles": {"root": {"padding": 16}}},
                "Alert": {"styles": {"title": {"fontWeight": 500}}},
                "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                "Badge": {"styles": {"root": {"fontWeight": 500}}},
                "Progress": {"styles": {"label": {"fontWeight": 500}}},
                "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
                "CodeHighlightTabs": {"styles": {"file": {"padding": 6, "border": "1px solid", "borderColor": "var(--mantine-color-default-border)"}}},
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
        children=dmc.Box([
            dcc.Location(id="url", refresh="callback-nav"),
            dcc.Store(id="color-scheme-storage", storage_type="local"),
            dcc.Store(id="initial-scroll-done", data=False),
            dmc.NotificationContainer(id="notification-container"),
             dmc.AppShell(
                [
                    create_header(data),
                    create_navbar(data),
                    create_navbar_drawer(data),
                    dmc.Box(
                        dmc.AppShellMain(children=page_container),
                        maw="100em"
                    )
                ],
                header={"height": 70},
                padding="lg",
                navbar={
                    "width": 280,
                    "breakpoint": "lg",
                    "collapsed": {"mobile": True},
                },
                aside={
                    "width": 275,
                    "breakpoint": "xl",
                    "collapsed": {"desktop": False, "mobile": True},
                },
            ),
        ], className="dmc-code", px={"base": 0, "xxl": 50}),
    ), id="direction", direction="ltr")


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


#
# clientside_callback(
#     """
#     (switchOn) => {
#        document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');
#        return window.dash_clientside.no_update
#     }
#     """,
#     Output("docs-color-scheme-switch", "id"),
#     Input("docs-color-scheme-switch", "checked"),
# )


@callback(
    Output("rtl-icon", "icon"),
    Output("direction", "direction"),
    Input("rtl-toggle", "n_clicks"),
    State("direction", "direction")
)
def toggle_direction(n, d):
    if n is None:
        return no_update

    new_dir = "ltr" if d == "rtl" else "rtl"
    return f"tabler:text-direction-{new_dir}", new_dir


clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks) {
            document.querySelector('#clipboard-target').click();
        }     
    }
    """,
    Input("copy-label", "n_clicks"),
    prevent_initial_call=True
)
