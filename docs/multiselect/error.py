import dash_mantine_components as dmc
from dash import Output, Input, callback

component = dmc.MultiSelect(
    data=["USDINR", "EURUSD", "USDTWD", "USDJPY"],
    id="multi-select-error",
    value=["USDJPY"],
    w=400,
)


@callback(Output("multi-select-error", "error"), Input("multi-select-error", "value"))
def select_value(value):
    return "Select at least 2." if len(value) < 2 else ""
