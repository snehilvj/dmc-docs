import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.Tab(
                    "Messages",
                    rightSection=dmc.Badge(
                        "6",
                        size="xs",
                        p=0,
                        variant="filled",
                        sx={"width": 16, "height": 16, "pointerEvents": "none"},
                    ),
                    value="messages",
                ),
                dmc.Tab(
                    "Settings",
                    rightSection=DashIconify(icon="tabler:alert-circle", width=16),
                    value="settings",
                ),
            ]
        ),
    ],
    value="messages",
)
