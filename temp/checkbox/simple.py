import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.Checkbox(id="checkbox-simple", label="I agree to sell my privacy", mb=10),
        dmc.Text(id="checkbox-output"),
    ]
)


@callback(Output("checkbox-output", "children"), Input("checkbox-simple", "checked"))
def checkbox(checked):
    return "True" if checked else "False"
