from datetime import datetime

import dash_mantine_components as dmc

component = dmc.Group(
    spacing="xl",
    children=[
        dmc.DatePickerInput(
            value=datetime.now().date(),
            valueFormat="ddd, MMM D YY",
            label="ddd, MMM D YY",
            w=200,
        ),
        dmc.DatePickerInput(
            value=datetime.now().date(),
            valueFormat="MMMM DD, YY",
            label="MMMM DD, YY",
            w=200,
        ),
        dmc.DatePickerInput(
            value=datetime.now().date(),
            valueFormat="DD-MM-YYYY",
            label="DD-MM-YYYY",
            w=200,
        ),
    ],
)
