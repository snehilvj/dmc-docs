from datetime import datetime

import dash_mantine_components as dmc

component = dmc.Group(
    spacing="xl",
    children=[
        dmc.DatePicker(
            date=datetime.now().date(), format="ddd, MMM D YY", label="ddd, MMM D YY"
        ),
        dmc.DatePicker(
            date=datetime.now().date(),
            format="MMMM DD, YY",
            label="MMMM DD, YY",
        ),
        dmc.DatePicker(
            date=datetime.now().date(),
            format="DD-MM-YYYY",
            label="DD-MM-YYYY",
        ),
    ],
)
