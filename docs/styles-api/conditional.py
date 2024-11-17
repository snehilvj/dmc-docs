from dash import  html, callback, Output, Input, State
import dash_mantine_components as dmc

component = html.Div([
    dmc.TextInput(
        id="styles-input",
        label="Required Input",
        required=True,
    ),
    dmc.Button("Submit", id="styles-submit-btn")
])

@callback(
    Output("styles-input", "styles"),
    Input("styles-submit-btn", "n_clicks"),
    State("styles-input", "value"),
    prevent_initial_call=True
)
def update_styles(n_clicks, value):
    if not value:
        return {
            "input": {"borderColor": "red"},
            "label": {"color": "red"}
        }
    return {
        "input": {"borderColor": "green"},
        "label": {"color": "green"}
    }

