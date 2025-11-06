import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.CustomCopyButton(
    value="Custom Copy demo",
    children={"function": "copyActionIcon"},
)
