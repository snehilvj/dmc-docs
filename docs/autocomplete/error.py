import dash_mantine_components as dmc
from dash import Output, Input, callback

component = dmc.Autocomplete(
    data=["USDINR", "EURUSD", "USDTWD", "USDJPY"],
    id="autocomplete-error",
    value="USDJPY",
    w=200,
)


@callback(Output("autocomplete-error", "error"), Input("autocomplete-error", "value"))
def select_value(value):
    return "JPY is not allowed!" if value == "USDJPY" else ""
