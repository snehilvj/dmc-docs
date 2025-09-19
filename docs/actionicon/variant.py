import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line"), color="blue", variant=variant
        )
        for variant in [
            "subtle",
            "filled",
            "outline",
            "light",
            "default",
            "transparent",
            "gradient",
            "white"
        ]
    ]
)
