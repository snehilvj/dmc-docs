import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.Tab(
                    "Messages",
                    icon=DashIconify(icon="tabler:message"),
                    value="messages",
                ),
                dmc.Tab(
                    "Settings",
                    icon=DashIconify(icon="tabler:settings"),
                    value="settings",
                ),
            ]
        ),
    ],
    value="messages",
)
