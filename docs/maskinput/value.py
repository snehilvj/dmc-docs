from dash import Input, Output, callback
import dash_mantine_components as dmc

component = dmc.Stack([
    dmc.MaskInput(
        id="phone-mask",
        label="Phone number",
        placeholder="(555) 123-4567",
        mask="(999) 999-9999",
    ),
    dmc.Box(id="phone-mask-output"),
])


@callback(
    Output("phone-mask-output", "children"),
    Input("phone-mask", "maskedValue"),
    Input("phone-mask", "value"),
    Input("phone-mask", "complete"),
)
def show_values(masked_value, value, complete):
    return [
        dmc.Text(f"Masked value: {masked_value}"),
        dmc.Text(f"Raw value: {value}"),
        dmc.Text(f"Complete: {complete}"),
    ]