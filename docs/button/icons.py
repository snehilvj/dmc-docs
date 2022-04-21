import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        dmc.Button(
            "Connect to Database",
            leftIcon=[DashIconify(icon="fluent:database-plug-connected-20-filled")],
        ),
        dmc.Button(
            "Load Data",
            variant="subtle",
            rightIcon=[DashIconify(icon="logos:twitter")],
            color="blue",
        ),
        dmc.Button(
            "Settings",
            variant="outline",
            leftIcon=[DashIconify(icon="fluent:settings-32-regular")],
        ),
    ]
)
