from datetime import datetime, timedelta

import dash_mantine_components as dmc

component = dmc.Group(
    spacing="xl",
    children=[
        dmc.DatePicker(value=datetime.now().date(), amountOfMonths=2, label="2 months"),
        dmc.DateRangePicker(
            value=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            amountOfMonths=2,
            label="3 months",
            style={"width": 330},
        ),
    ],
)
