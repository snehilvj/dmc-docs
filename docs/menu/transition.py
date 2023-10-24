import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Menu(
    [
        dmc.MenuTarget(dmc.Button("Click for options!")),
        dmc.MenuDropdown(
            [
                dmc.MenuItem(
                    "External Link",
                    href="https://www.github.com/snehilvj",
                    target="_blank",
                    icon=DashIconify(icon="radix-icons:external-link"),
                ),
                dmc.MenuItem("Useless Button", n_clicks=0),
            ]
        ),
    ],
    transitionProps={"transition": "rotate-right", "duration": 150},
)
