from datetime import date
from dateutil.relativedelta import relativedelta

import dash_mantine_components as dmc

today = date.today()
start_of_month = lambda months: (today.replace(day=1) + relativedelta(months=months)).isoformat()

component = dmc.MonthPickerInput(
    label="With presets",
    placeholder="Select month",
    presets=[
        {"value": start_of_month(0), "label": "This month"},
        {"value": start_of_month(1), "label": "Next month"},
        {"value": start_of_month(-1), "label": "Last month"},
        {"value": start_of_month(6), "label": "In 6 months"},
        {"value": start_of_month(12), "label": "Next year"},
        {"value": start_of_month(-12), "label": "Last year"},
    ],
)