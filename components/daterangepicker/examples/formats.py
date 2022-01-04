from datetime import datetime, timedelta

import dash_mantine_components as dmc

component = dmc.Group(
    spacing="xl",
    children=[
        dmc.DateRangePicker(
            dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            format="ddd, MMM D YY",
            label="ddd, MMM D YY",
        ),
        dmc.DateRangePicker(
            dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            format="MMMM DD, YY",
            label="MMMM DD, YY",
        ),
        dmc.DateRangePicker(
            dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            format="DD-MM-YYYY",
            label="DD-MM-YYYY",
        ),
    ],
)
