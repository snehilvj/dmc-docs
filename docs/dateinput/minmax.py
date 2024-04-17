from datetime import datetime, timedelta

import dash_mantine_components as dmc

component = dmc.DateInput(
    minDate=datetime.now(),
    maxDate=datetime.now() + timedelta(days=7),
    placeholder="Date input",
    label="Select valid date",
    w=250,
)
