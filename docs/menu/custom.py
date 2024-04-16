from dash_iconify import DashIconify
import dash_mantine_components as dmc

component = dmc.Menu(
    [
        dmc.MenuTarget(dmc.ActionIcon(DashIconify(icon="tabler:user"))),
        dmc.MenuDropdown(
            [
                dmc.MenuItem(
                    "External Link",
                    href="https://www.github.com/snehilvj",
                    target="_blank",
                    leftSection=DashIconify(icon="radix-icons:external-link"),
                ),
                dmc.MenuItem("Useless Button", n_clicks=0),
            ]
        ),
    ]
)
