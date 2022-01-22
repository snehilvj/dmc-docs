from datetime import datetime, timedelta

import dash_mantine_components as dmc
from dash import Output, Input
from dash import callback  # no-prism

component = dmc.DateRangePicker(
    id="datepicker-range-error",
    value=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
    label="Date",
    required=True,
    clearable=False,
    style={"width": 330},

)


@callback(
    Output("datepicker-range-error", "error"), Input("datepicker-range-error", "value")
)
def datepicker_error(dates):
    start = datetime.strptime(dates[0], "%Y-%M-%d").day
    end = datetime.strptime(dates[1], "%Y-%M-%d").day
    return "Diff between the dates should be more than 4." if (end - start) < 5 else ""
