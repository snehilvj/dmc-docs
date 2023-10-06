from datetime import datetime, timedelta, date

import dash_mantine_components as dmc

component =dmc.DatePicker(
    minDate=date(2020, 8, 5),
    type="range",
    value=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
    allowSingleDateInRange=True,
)
