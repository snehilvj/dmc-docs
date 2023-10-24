import dash_mantine_components as dmc
from dash import Input, Output, html, callback

component = html.Div(
    [
        dmc.DateInput(
            id="dateinput2",
            label="Enter a date",
            description="You can type a date or select from the calendar",
            style={"width": 350},
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-dateinput2"),
    ]
)


@callback(Output("selected-dateinput2", "children"), Input("dateinput2", "value"))
def update_output(d):
    prefix = "You entered: "
    if d:
        return prefix + d
    else:
        return ""
