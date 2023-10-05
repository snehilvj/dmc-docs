from datetime import datetime, date

import dash_mantine_components as dmc
from dash import Input, Output, html, callback
from dash.exceptions import PreventUpdate

component = html.Div(
    [
        dmc.DatePickerInput(
            id="date-picker-input",
            label="Start Date",
            description="You can also provide a description",
            minDate=date(2020, 8, 5),
            value=datetime.now().date(),  # or string in the format "YYYY-MM-DD"
            style={"width": 200},
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date-input"),
    ]
)


@callback(
    Output("selected-date-input", "children"), Input("date-picker-input", "value")
)
def update_output(d):
    prefix = "You have selected: "
    if d:
        return prefix + d
    else:
        raise PreventUpdate
