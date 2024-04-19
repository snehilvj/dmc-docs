import dash_mantine_components as dmc

from dash_iconify import DashIconify

component = dmc.Button(
    "GitHub",
    leftSection=DashIconify(icon="radix-icons:github-logo", width=20),
    rightSection=dmc.Badge("3", circle=True, color="gray"),
)
