import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.TextInput(
    label="Your Email",
    style={"width": 200},
    placeholder="Your Email",
    icon=DashIconify(icon="ic:round-alternate-email"),
)
