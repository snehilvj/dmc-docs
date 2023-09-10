import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.Checkbox(
            id="checkbox-state", label="I agree to sell my privacy", checked=True, mb=10
        ),
        dmc.Text(id="checkbox-output"),
    ]
)


@callback(Output("checkbox-output", "children"), Input("checkbox-state", "checked"))
def checkbox(checked):
    return str(checked)
