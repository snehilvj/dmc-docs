from datetime import datetime, timedelta

import dash_mantine_components as dmc

component = dmc.DateRangePicker(
    dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
    clearable=False,
    dropdownType="modal",
)
