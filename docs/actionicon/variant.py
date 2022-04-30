import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line"), color="blue", variant="hover"
        ),
        dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line"), color="blue", variant="default"
        ),
        dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line"),
            color="blue",
            variant="transparent",
        ),
        dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line"), color="blue", variant="filled"
        ),
        dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line"), color="blue", variant="light"
        ),
        dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line"), color="blue", variant="outline"
        ),
    ]
)
