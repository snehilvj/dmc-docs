import dash_mantine_components as dmc
from dash import html, Output, Input

component = html.Div(
    [
        dmc.Checkbox(
            id="checkbox",
            label="I agree to sell my privacy",
        ),
        dmc.Space(h=10),  # no-prism
        dmc.Text(id="checkbox-output"),
    ]
)


@app.callback(Output("checkbox-output", "children"), Input("checkbox", "checked"))
def checkbox(checked):
    return "True" if checked else "False"
