from datetime import date

import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        dmc.DatePicker(value=date.today(), icon=DashIconify(icon="clarity:date-line")),
        dmc.Button(
            "Open Settings",
            leftIcon=DashIconify(icon="carbon:settings-check", width=20),
        ),
    ]
)
