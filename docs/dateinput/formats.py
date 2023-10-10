from datetime import datetime

import dash_mantine_components as dmc

component = dmc.Group(
    spacing="xl",
    children=[
        dmc.DateInput(
            value=datetime.now().date(),
            valueFormat="ddd, MMM D YY",
            label="ddd, MMM D YY",
        ),
        dmc.DateInput(
            value=datetime.now().date(),
            valueFormat="MMMM DD, YY",
            label="MMMM DD, YY",
        ),
        dmc.DateInput(
            value=datetime.now().date(),
            valueFormat="DD-MM-YYYY",
            label="DD-MM-YYYY",
        ),
    ],
)
