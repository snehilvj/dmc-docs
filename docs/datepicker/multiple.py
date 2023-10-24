from datetime import datetime, date, timedelta

import dash_mantine_components as dmc
from dash import Input, Output, html, callback, no_update


component = html.Div(
    [
        dmc.DatePicker(
            id="date-picker-multiple",
            minDate=date(2020, 8, 5),
            value=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            type="multiple",
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date-multiple"),
    ]
)


@callback(
    Output("selected-date-multiple", "children"), Input("date-picker-multiple", "value")
)
def update_output(dates):
    prefix = "You have selected: "
    if dates:
        return prefix + ",   ".join(dates)
    else:
        return no_update
