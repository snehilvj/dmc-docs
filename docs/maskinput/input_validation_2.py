from dash import Input, Output, State, callback
import dash_mantine_components as dmc

component = dmc.MaskInput(
    id="mask-input-validation",
    label="Phone number",
    placeholder="(___) ___-____",
    w=300,
    required=True,
    mask="(999) 999-9999"
)

@callback(
    Output("mask-input-validation", "success"),
    Output("mask-input-validation", "error"),
    Input("mask-input-validation", "n_blur"),
    State("mask-input-validation", "complete"),
)
def mask_input_validation(n_blur, complete):
    if n_blur is None:
        return "", ""
    if complete:
        return True, ""
    else:
        return "", "Please enter phone number with area code"
