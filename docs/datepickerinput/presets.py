from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import dash_mantine_components as dmc


today = date.today()

component = dmc.DatePickerInput(
    label="With presets",
    placeholder="Select date",
    presets=[
        {
            "value": (today - timedelta(days=1)).isoformat(),
            "label": "Yesterday",
        },
        {
            "value": today.isoformat(),
            "label": "Today",
        },
        {
            "value": (today + timedelta(days=1)).isoformat(),
            "label": "Tomorrow",
        },
        {
            "value": (today + relativedelta(months=1)).isoformat(),
            "label": "Next month",
        },
        {
            "value": (today + relativedelta(years=1)).isoformat(),
            "label": "Next year",
        },
        {
            "value": (today - relativedelta(months=1)).isoformat(),
            "label": "Last month",
        },
        {
            "value": (today - relativedelta(years=1)).isoformat(),
            "label": "Last year",
        },
    ],
    maw=200
)
