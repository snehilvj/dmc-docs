from datetime import datetime

import dash_mantine_components as dmc
from dash import Output, Input

component = dmc.DatePicker(
    id="datepicker-error",
    date=datetime.now().date(),
    label="Date",
    required=True,
    clearable=False,
)


@app.callback(Output("datepicker-error", "error"), Input("datepicker-error", "date"))
def datepicker_error(date):
    day = datetime.strptime(date, "%Y-%M-%d").day
    return "Please select an even date." if day % 2 else ""
