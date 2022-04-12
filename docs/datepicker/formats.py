from datetime import datetime

import dash_mantine_components as dmc

component = dmc.Group(
    spacing="xl",
    children=[
        dmc.DatePicker(
            value=datetime.now().date(),
            inputFormat="ddd, MMM D YY",
            label="ddd, MMM D YY",
        ),
        dmc.DatePicker(
            value=datetime.now().date(),
            inputFormat="MMMM DD, YY",
            label="MMMM DD, YY",
        ),
        dmc.DatePicker(
            value=datetime.now().date(),
            inputFormat="DD-MM-YYYY",
            label="DD-MM-YYYY",
        ),
    ],
)
