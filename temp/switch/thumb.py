import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Switch(
    thumbIcon=DashIconify(
        icon="tabler:walk", width=16, color=dmc.theme.DEFAULT_COLORS["teal"][5]
    ),
    size="lg",
    color="teal",
    checked=True,
)
