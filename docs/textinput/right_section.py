import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.TextInput(
    label="Your Email:",
    style={"width": 150},
    placeholder='Your Email',
    rightSection=[DashIconify(icon='ic:round-alternate-email')],
)
