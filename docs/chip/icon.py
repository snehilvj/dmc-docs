import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Chip(
    "Forbidden",
    icon=DashIconify(icon="bi-x-circle"),
    color="red",
    checked=True,
    controlled=True,
    m="sm",
)
