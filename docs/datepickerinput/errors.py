from datetime import datetime

import dash_mantine_components as dmc
from dash import Output, Input, callback

component = dmc.DatePickerInput(
    id="datepickerinput-error",
    value=datetime.now().date(),
    label="Date",
    required=True,
    clearable=False,
    w=200,
)


@callback(Output("datepickerinput-error", "error"), Input("datepickerinput-error", "value"))
def datepicker_error(date):
    day = datetime.strptime(date, "%Y-%M-%d").day
    return "Please select an even date." if day % 2 else ""
