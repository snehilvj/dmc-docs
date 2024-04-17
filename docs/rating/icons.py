import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Rating(
    value=1,
    emptySymbol=DashIconify(icon="tabler:sun"),
    fullSymbol=DashIconify(icon="tabler:moon"),
)
