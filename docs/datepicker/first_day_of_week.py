from datetime import datetime

import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.DatePicker(
            value=datetime.now().date(),
            firstDayOfWeek=0
        ),
        dmc.DatePicker(
            value=datetime.now().date(),
            firstDayOfWeek=6
        )
    ]
)
