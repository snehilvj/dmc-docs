import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        dmc.Button(
            "Connect to Database",
            leftSection=DashIconify(icon="fluent:database-plug-connected-20-filled"),
        ),
        dmc.Button(
            "Load Data",
            variant="subtle",
            rightSection=DashIconify(icon="logos:twitter"),
            color="blue",
        ),
        dmc.Button(
            "Settings",
            variant="outline",
            leftSection=DashIconify(icon="fluent:settings-32-regular"),
        ),
    ]
)
