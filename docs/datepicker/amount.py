from datetime import datetime, timedelta

import dash_mantine_components as dmc

component = dmc.DatePicker(
    value=datetime.now().date(),
    numberOfColumns=2,
)