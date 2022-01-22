from datetime import datetime, timedelta

import dash_mantine_components as dmc

component = dmc.Group(
    spacing="xl",
    children=[
        dmc.DateRangePicker(
            value=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            inputFormat="ddd, MMM D YY",
            label="ddd, MMM D YY",
            style={"width": 330},  # no-prism
        ),
        dmc.DateRangePicker(
            value=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            inputFormat="MMMM DD, YY",
            label="MMMM DD, YY",
            style={"width": 330},  # no-prism
        ),
        dmc.DateRangePicker(
            value=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            inputFormat="DD-MM-YYYY",
            label="DD-MM-YYYY",
            style={"width": 330},  # no-prism
        ),
    ],
)
