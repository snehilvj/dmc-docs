from datetime import datetime, timedelta, date

import dash_mantine_components as dmc
from dash import Input, Output, html
from dash.exceptions import PreventUpdate

component = html.Div(
    [
        dmc.DateRangePicker(
            id="date-range-picker",
            label="Date Range",
            description="You can also provide a description",
            minDate=date(2020, 8, 5),
            maxDate=date(2022, 9, 19),
            dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
        ),
        dmc.Space(h=10),  # no-prism
        dmc.Text(id="selected-date-date-range-picker"),
    ]
)


@app.callback(
    Output("selected-date-date-range-picker", "children"),
    Input("date-range-picker", "dates"),
)
def update_output(dates):
    prefix = "You have selected: "
    if dates:
        return prefix + "   -   ".join(dates)
    else:
        raise PreventUpdate
