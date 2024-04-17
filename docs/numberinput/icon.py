import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.NumberInput(
    label="Your weight in kg",
    description="From 0 to infinity, in steps of 5",
    value=5,
    min=0,
    step=5,
    leftSection=DashIconify(icon="fa6-solid:weight-scale"),
    w=250,
)
