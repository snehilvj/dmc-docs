import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line"),
            color="blue",
            variant="gradient",
            gradient=gradient
        )
        for gradient in [
            {"from": "red", "to": "blue", "deg": 90 },
            {"from": "red", "to": "blue", "deg": 180},
            {"from": "teal", "to": "yellow", "deg": 90},
            {"from": "teal", "to": "yellow", "deg": 180}
         ]
    ]
)
