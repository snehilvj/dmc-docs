from dash_iconify import DashIconify
import dash_mantine_components as dmc

component = dmc.Menu(
    [
        dmc.MenuTarget(dmc.Button("Hover for options!")),
        dmc.MenuDropdown(
            [
                dmc.MenuLabel("Application"),
                dmc.MenuItem("Settings", leftSection=DashIconify(icon="tabler:settings")),
                dmc.MenuItem("Messages", leftSection=DashIconify(icon="tabler:message")),
                dmc.MenuItem("Gallery", leftSection=DashIconify(icon="tabler:photo")),
                dmc.MenuItem("Search", leftSection=DashIconify(icon="tabler:search")),
                dmc.MenuDivider(),
                dmc.MenuLabel("Danger Zone"),
                dmc.MenuItem(
                    "Transfer my data",
                    leftSection=DashIconify(icon="tabler:arrows-left-right"),
                ),
                dmc.MenuItem(
                    "Delete my account",
                    leftSection=DashIconify(icon="tabler:trash"),
                    color="red",
                ),
            ]
        ),
    ],
    trigger="hover",
)
