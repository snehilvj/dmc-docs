"""
Alt Layout
Navbar and Aside are rendered on top on Header and Footer

"""

import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, callback, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

logo = "https://github.com/user-attachments/assets/c1ff143b-4365-4fd1-880f-3e97aab5c302"

layout = dmc.AppShell(
    [
        dmc.AppShellHeader(
            dmc.Group(
                [
                    dmc.Burger(id="burger", size="sm", hiddenFrom="sm", opened=False),
                    dmc.Image(src=logo, h=40),
                    dmc.Title("Demo App", c="blue"),
                ],
                h="100%",
                px="md",
            )
        ),
        dmc.AppShellNavbar(
            p="md",
            children=[
                dmc.Group(
                    [
                        dmc.Burger(
                            id="navbar-burger", size="sm", hiddenFrom="sm", opened=False
                        ),
                        dmc.Text("Navbar"),
                    ]
                ),
                *[dmc.Skeleton(height=28, mt="sm", animate=False) for _ in range(15)],
            ],
        ),
        dmc.AppShellMain(
            "Alt layout – Navbar and Aside are rendered on top of Header and Footer"
        ),
        dmc.AppShellAside("Aside", p="md"),
        dmc.AppShellFooter("Footer", p="md"),
    ],
    layout="alt",
    header={"height": 60},
    footer={"height": 60},
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    aside={
        "width": 300,
        "breakpoint": "md",
        "collapsed": {"desktop": False, "mobile": True},
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
    navbar["collapsed"] = {"mobile": not opened}
    return navbar


if __name__ == "__main__":
    app.run(debug=True)
