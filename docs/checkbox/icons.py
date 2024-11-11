import dash_mantine_components as dmc
from dash_iconify import DashIconify


component = dmc.Stack([
    dmc.Checkbox(
        label="Custom checked icon",
        checked=True,
        icon=DashIconify(icon="ion:bag-check-sharp"),
        size="lg",
        p=0,
    ),
    dmc.Checkbox(
        label="Custom intermediate icons",
        indeterminate=True,
        indeterminateIcon=DashIconify(icon="material-symbols:indeterminate-question-box"),
        size="lg"
    )
])