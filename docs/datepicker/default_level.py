from datetime import datetime

import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.DatePicker(value=datetime.now().date(), level="decade"),
        dmc.DatePicker(value=datetime.now().date(), level="year"),
    ]
)
