from datetime import datetime, timedelta

import dash_mantine_components as dmc

component = dmc.YearPickerInput(
    minDate=datetime(2021, 1, 1),
    maxDate=datetime(2028, 1, 1),
    value=datetime(2021, 1, 1),
    placeholder="Date input",
    label="Select valid date",
    w=250,
)
