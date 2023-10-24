import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Rating(
    value=1,
    emptySymbol=DashIconify(icon="fa-regular:sun"),
    fullSymbol=DashIconify(icon="fa-regular:moon")
)

