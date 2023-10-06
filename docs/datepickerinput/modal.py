from datetime import datetime

import dash_mantine_components as dmc

component = dmc.DatePickerInput(
    value=datetime.now().date(),
    dropdownType="modal",
    w=200,
    modalProps={"zIndex": 2000},
)
