from datetime import date
from dateutil.relativedelta import relativedelta

import dash_mantine_components as dmc

today = date.today()
start_of_month = lambda months: (today.replace(day=1) + relativedelta(months=months)).isoformat()
start_of_year = lambda years: date(today.year + years, 1, 1).isoformat()

component = dmc.MonthPickerInput(
    type="range",
    label="With presets",
    placeholder="Select months range",
    presets=[
        {
            "value": [start_of_month(-3), start_of_month(0)],
            "label": "Last 3 months",
        },
        {
            "value": [start_of_month(-6), start_of_month(0)],
            "label": "Last 6 months",
        },
        {
            "value": [start_of_year(0), start_of_month(0)],
            "label": "This year",
        },
        {
            "value": [start_of_year(-1), date(today.year - 1, 12, 1).isoformat()],
            "label": "Last year",
        },
    ],
)