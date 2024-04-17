import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.PasswordInput(
    label="Your password:",
    w=250,
    placeholder="Your password",
    leftSection=DashIconify(icon="bi:shield-lock"),
)
