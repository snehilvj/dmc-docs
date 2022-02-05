import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Group(
    children=[
        dmc.TimeInput(
            label="Enter Time:", icon=[DashIconify(icon="akar-icons:clock")],
        ),
        dmc.TimeInput(
            label="Enter Time:",
            iconWidth=90,
            icon=[DashIconify(icon="akar-icons:clock")],
        ),
    ]
)
