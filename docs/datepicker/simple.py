from datetime import datetime, date

import dash_mantine_components as dmc
from dash import Input, Output, html, callback, no_update

component = html.Div(
    [
        dmc.DatePicker(
            id="date-picker",
            value=datetime.now().date(),
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date"),
    ]
)


@callback(Output("selected-date", "children"), Input("date-picker", "value"))
def update_output(d):
    prefix = "You have selected: "
    if d:
        return prefix + d
    else:
        return no_update
