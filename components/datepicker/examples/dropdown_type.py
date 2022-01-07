from datetime import datetime

import dash_mantine_components as dmc

component = dmc.DatePicker(
    date=datetime.now().date(),
    clearable=False,
    dropdownType="modal",
)
