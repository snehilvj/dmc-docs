from datetime import datetime

import dash_mantine_components as dmc

component = dmc.Group(
    spacing="xl",
    children=[
        dmc.DatePicker(date=datetime.now().date(), amountOfMonths=2, label="2 months"),
        dmc.DatePicker(date=datetime.now().date(), amountOfMonths=3, label="3 months"),
    ],
)
