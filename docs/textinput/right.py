import dash_mantine_components as dmc
from dash_iconify import DashIconify


component = dmc.Stack(
    children=[
        dmc.TextInput(
            style={"width": 200},
            placeholder="9876543210",
            rightSection=DashIconify(icon="emojione-v1:mobile-phone"),
        ),
        dmc.TextInput(
            style={"width": 200},
            placeholder="9876543210",
            rightSection=dmc.Loader(size="xs"),
        ),
    ],
)
