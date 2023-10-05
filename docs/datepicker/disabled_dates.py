from datetime import datetime, timedelta

import dash_mantine_components as dmc

today = datetime.now().date()

component = dmc.DatePicker(
    value=today,
    disabledDates=[today + timedelta(days=1), today + timedelta(days=3)],
)
