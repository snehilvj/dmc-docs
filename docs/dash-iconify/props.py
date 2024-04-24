import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    [
        DashIconify(icon="ion:logo-github", width=30, rotate=1, flip="horizontal"),
        DashIconify(icon="flat-ui:settings", width=30),
        DashIconify(
            icon="feather:info",
            color=dmc.DEFAULT_THEME["colors"]["yellow"][5],
            width=30,
        ),
    ]
)
