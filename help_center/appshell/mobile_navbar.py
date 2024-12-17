"""
Mobile only navbar

Navbar is only visible on mobile, links that are rendered in the header
on desktop are hidden on mobile in header and rendered in navbar instead.
"""

import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, callback, _dash_renderer

_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

logo = "https://github.com/user-attachments/assets/c1ff143b-4365-4fd1-880f-3e97aab5c302"
buttons = [
    dmc.Button("Home", variant="subtle", color="gray"),
    dmc.Button("Blog", variant="subtle", color="gray"),
    dmc.Button("Contacts", variant="subtle", color="gray"),
    dmc.Button("Support", variant="subtle", color="gray"),
]

layout = dmc.AppShell(
    [
        dmc.AppShellHeader(
            dmc.Group(
                [
                    dmc.Group(
                        [
                            dmc.Burger(
                                id="burger",
                                size="sm",
                                hiddenFrom="sm",
                                opened=False,
                            ),
                            dmc.Image(src=logo, h=40),
                            dmc.Title("Demo App", c="blue"),
                        ]
                    ),
                    dmc.Group(
                        children=buttons,
                        ml="xl",
                        gap=0,
                        visibleFrom="sm",
                    ),
                ],
                justify="space-between",
                style={"flex": 1},
                h="100%",
                px="md",
            ),
        ),
        dmc.AppShellNavbar(
            id="navbar",
            children=buttons,
            py="md",
            px=4,
        ),
        dmc.AppShellMain(
            "Navbar is only visible on mobile, links that are rendered in the header on desktop are hidden on mobile in header and rendered in navbar instead."
        ),
    ],
    header={"height": 60},
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"desktop": True, "mobile": True},
    },
    padding="md",
    id="appshell",
)

app.layout = dmc.MantineProvider(layout)


@callback(
    Output("appshell", "navbar"),
    Input("burger", "opened"),
    State("appshell", "navbar"),
)
def toggle_navbar(opened, navbar):
    navbar["collapsed"] = {"mobile": not opened, "desktop": True}
    return navbar


if __name__ == "__main__":
    app.run(debug=True)
