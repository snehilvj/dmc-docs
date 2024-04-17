import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab(
                    "Messages",
                    rightSection=dmc.Badge(
                        "6", size="xs", p=0, variant="filled", circle=True
                    ),
                    value="messages",
                ),
                dmc.TabsTab(
                    "Settings",
                    rightSection=DashIconify(icon="tabler:alert-circle", width=16),
                    value="settings",
                ),
            ]
        ),
    ],
    value="messages",
)
