from datetime import datetime

import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.DatePicker(
            value=datetime.now().date(),
            maxLevel="year"
        ),
        dmc.DatePicker(
            value=datetime.now().date(),
            maxLevel="month"
        )
    ]
)
