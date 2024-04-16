import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.PasswordInput(
    label="Your password:",
    style={"width": 250},
    placeholder="Your password",
    leftSection=DashIconify(icon="bi:shield-lock"),
)
