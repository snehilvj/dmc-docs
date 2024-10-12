from datetime import datetime, timedelta

import dash_mantine_components as dmc

component = dmc.MonthPickerInput(
    minDate=datetime(2022, 1, 1),
    maxDate=datetime(2022, 8, 1),
    value=datetime(2022, 1, 1),
    placeholder="Date input",
    label="Select valid date",
    w=250,
)