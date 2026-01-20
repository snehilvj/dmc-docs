from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import dash_mantine_components as dmc


now = datetime.now()

component = dmc.DateTimePicker(
    label="Pick date and time",
    placeholder="Pick date and time",
    presets=[
        {
            "value": (now - timedelta(days=1)).isoformat(),
            "label": "Yesterday",
        },
        {
            "value": now.isoformat(),
            "label": "Today",
        },
        {
            "value": (now + timedelta(days=1)).isoformat(),
            "label": "Tomorrow",
        },
        {
            "value": (now + relativedelta(months=1)).isoformat(),
            "label": "Next month",
        },
        {
            "value": (now + relativedelta(years=1)).isoformat(),
            "label": "Next year",
        },
        {
            "value": (now - relativedelta(months=1)).isoformat(),
            "label": "Last month",
        },
        {
            "value": (now - relativedelta(years=1)).isoformat(),
            "label": "Last year",
        },
    ]
)
