
from datetime import datetime, timedelta

import dash_mantine_components as dmc

today = datetime.now().date()

component = dmc.Stack([
    dmc.DatePicker(
        value=today,
        disabledDates=[today + timedelta(days=1), today + timedelta(days=3)],
        m="lg"
    ),
    dmc.DatePicker(
        value="2024-11-05",
        defaultDate="2024-11-01",
        disabledDates=["2024-11-06", "2024-11-07",  "2024-11-08"],
        m="lg"
    )
], align="center")
