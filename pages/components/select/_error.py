import dash_mantine_components as dmc
from dash import Output, Input
from dash import callback  # no-prism

component = dmc.Select(
    data=["USDINR", "EURUSD", "USDTWD", "USDJPY"],
    id="select-error",
    value="USDJPY",
    style={"width": 200},
)


@callback(Output("select-error", "error"), Input("select-error", "value"))
def select_value(value):
    return "JPY is not allowed!" if value == "USDJPY" else ""
