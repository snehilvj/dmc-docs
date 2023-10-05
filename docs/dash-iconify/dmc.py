from datetime import date

import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        dmc.Alert(
            icon=DashIconify(icon="radix-icons:cross-circled"),
            children="Error",
            color="red",
        ),
        dmc.Button(
            "Open Settings",
            leftIcon=DashIconify(icon="carbon:settings-check", width=20),
        ),
    ]
)
