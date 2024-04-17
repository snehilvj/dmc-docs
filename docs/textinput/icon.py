import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.TextInput(
    label="Your Email",
    w=200,
    placeholder="Your Email",
    leftSection=DashIconify(icon="ic:round-alternate-email"),
)
