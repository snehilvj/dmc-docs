from datetime import datetime, timedelta

import dash_mantine_components as dmc

component = dmc.Group(
    spacing="xl",
    children=[
        dmc.DateRangePicker(
            dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            amountOfMonths=2,
            label="2 months",
        ),
        dmc.DateRangePicker(
            dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            amountOfMonths=3,
            label="3 months",
        ),
    ],
)
