import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Button(
    "Settings",
    leftSection=DashIconify(icon="ic:baseline-settings-input-composite"),
    styles={"root": {"fontWeight": 400}, "section": {"width": 100}},
)
