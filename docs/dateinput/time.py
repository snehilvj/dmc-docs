from datetime import datetime

import dash_mantine_components as dmc
from dash import Output, callback, Input, html

component = html.Div(
    [
        dmc.DateInput(
            id="datetime-time",
            valueFormat="DD/MM/YYYY HH:mm:ss",
            label="Date and Time input",
            value=datetime.now(),
            w=250,
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-datetime"),
    ]
)


@callback(Output("selected-datetime", "children"), Input("datetime-time", "value"))
def update_output(d):
    prefix = "You entered: "
    if d:
        return prefix + d
    else:
        return ""
