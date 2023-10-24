import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Button(
    "Settings",
    leftIcon=DashIconify(icon="ic:baseline-settings-input-composite"),
    styles={"root": {"fontWeight": 400}, "leftIcon": {"width": 100}},
)
