from datetime import datetime, date, timedelta

import dash_mantine_components as dmc
from dash import Input, Output, html, callback, no_update


component = html.Div(
    [
        dmc.DatePickerInput(
            id="date-picker-input-multiple",
            label="Pick dates",
            description="Pick one or more dates",
            minDate=date(2020, 8, 5),
            value=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            style={"width": 400},
            type="multiple",
            placeholder="Pick dates",
            maw=400,
            clearable=True,
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date-input-multiple"),
    ]
)


@callback(
    Output("selected-date-input-multiple", "children"),
    Input("date-picker-input-multiple", "value"),
)
def update_output(dates):
    prefix = "You have selected: "
    if dates:
        return prefix + ",   ".join(dates)
    else:
        return no_update
