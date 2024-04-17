import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab(
                    "Messages",
                    leftSection=DashIconify(icon="tabler:message"),
                    value="messages",
                ),
                dmc.TabsTab(
                    "Settings",
                    leftSection=DashIconify(icon="tabler:settings"),
                    value="settings",
                ),
            ]
        ),
    ],
    value="messages",
)
