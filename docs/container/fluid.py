import dash_mantine_components as dmc
from dash import html


component = dmc.Container(
    "Fluid container has 100% max-width",
    fluid=True,
    h=50,
    bg="var(--mantine-color-blue-light)"
)
