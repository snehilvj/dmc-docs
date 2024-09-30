from datetime import datetime

import dash_mantine_components as dmc

component = dmc.DateTimePicker(
    clearable=True,
    value=datetime.now(),
    label="Pick date and time (clearable)",
    placeholder="Pick Date and time",
)
