from datetime import datetime

import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.DatePickerInput(
            value=datetime.now().date(),
            label="Date not clearable",
            w=200,
        ),
        dmc.DatePickerInput(
            value=datetime.now().date(),
            label="Date clearable",
            w=200,
            clearable=True,
        ),
    ]
)
