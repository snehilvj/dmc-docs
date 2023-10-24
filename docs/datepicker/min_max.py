from datetime import date

import dash_mantine_components as dmc

component =dmc.DatePicker(
    minDate=date(2023, 8, 1),
    maxDate=date(2023, 8, 15),
    value="2023-08-11",
    # defaultDate = "2023-08"    Need to add this prop to display correct month at start
)
