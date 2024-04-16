from datetime import datetime

import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.DatePicker(
            value=datetime.now().date(),
            label="Date not clearable",
            style={"width": 200},
        ),
        dmc.DatePicker(
            value=datetime.now().date(),
            label="Date clearable",
            style={"width": 200},
            clearable=True,
        ),
    ]
)
