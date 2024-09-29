from datetime import datetime

import dash_mantine_components as dmc

component = dmc.YearPickerInput(
    clearable=True,
    value=datetime.now(),
    label="Pick date (clearable)",
    placeholder="Pick Date",
)
