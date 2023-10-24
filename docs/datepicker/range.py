from datetime import datetime, timedelta, date

import dash_mantine_components as dmc
from dash import Input, Output, html, callback
from dash.exceptions import PreventUpdate

component = html.Div(
    [
        dmc.DatePicker(
            id="date-range-picker",
            minDate=date(2020, 8, 5),
            type="range",
            value=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date-range-picker"),
    ]
)


@callback(
    Output("selected-date-range-picker", "children"),
    Input("date-range-picker", "value"),
)
def update_output(dates):
    prefix = "You have selected from "
    if None not in dates:
        return prefix + "   to   ".join(dates)
    else:
        raise PreventUpdate
