from datetime import datetime, timedelta, date

import dash_mantine_components as dmc
from dash import Input, Output, html, callback
from dash.exceptions import PreventUpdate

component = html.Div(
    [
        dmc.DatePickerInput(
            id="date-input-range-picker",
            label="Date Range",
            description="Select a date range",
            minDate=date(2020, 8, 5),
            type="range",
            value=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            maw=400,
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date-input-range-picker"),
    ]
)


@callback(
    Output("selected-date-input-range-picker", "children"),
    Input("date-input-range-picker", "value"),
)
def update_output(dates):
    prefix = "You have selected from "
    if None not in dates:
        return prefix + "   to   ".join(dates)
    else:
        raise PreventUpdate
