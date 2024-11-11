import dash_mantine_components as dmc
from dash_iconify import DashIconify


component = dmc.Stack([
    dmc.Checkbox(
        label="Custom checked icon",
        checked=True,
        icon=DashIconify(icon="ion:bag-check-sharp"),
        size="lg",
    ),
    dmc.Checkbox(
        label="Custom indeterminate icons",
        indeterminate=True,
        indeterminateIcon=DashIconify(icon="mdi:dots-circle", ),
        size="lg",
    ),
])