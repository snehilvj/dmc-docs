from dash import Input, Output, State, callback
import dash_mantine_components as dmc

component = dmc.MaskInput(
    id="mask-input-complete",
    label="Phone number",
    placeholder="(___) ___-____",
    w=300,
    required=True,
    mask="(999) 999-9999"
)

@callback(
    Output("mask-input-complete", "success"),
    Output("mask-input-complete", "error"),
    Input("mask-input-complete", "complete"),
)
def mask_input_complete(complete):
    if complete:
        return True, ""
    else:
        return "", "Please enter phone number with area code"
