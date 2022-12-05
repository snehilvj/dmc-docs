from dash_iconify import DashIconify
import dash_mantine_components as dmc

component = dmc.Menu(
    [
        dmc.MenuTarget(dmc.Button("Click for options!")),
        dmc.MenuDropdown(
            [
                dmc.MenuLabel("Application"),
                dmc.MenuItem("Settings", icon=DashIconify(icon="tabler:settings")),
                dmc.MenuItem("Messages", icon=DashIconify(icon="tabler:message")),
                dmc.MenuItem("Gallery", icon=DashIconify(icon="tabler:photo")),
                dmc.MenuItem("Search", icon=DashIconify(icon="tabler:search")),
                dmc.MenuDivider(),
                dmc.MenuLabel("Danger Zone"),
                dmc.MenuItem(
                    "Transfer my data",
                    icon=DashIconify(icon="tabler:arrows-left-right"),
                ),
                dmc.MenuItem(
                    "Delete my account",
                    icon=DashIconify(icon="tabler:trash"),
                    color="red",
                ),
            ]
        ),
    ], trigger="hover"
)
