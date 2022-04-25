import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Select(
    data=["USDINR", "EURUSD", "USDTWD", "USDJPY"],
    value="USDJPY",
    label="Currency Pair",
    required=True,
    style={"width": 200},
    icon=[DashIconify(icon="radix-icons:magnifying-glass")],
    rightSection=[DashIconify(icon="radix-icons:chevron-down")],
)
