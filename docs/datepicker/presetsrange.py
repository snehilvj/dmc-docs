from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import dash_mantine_components as dmc


today = date.today()

component = dmc.Center(
    dmc.DatePicker(
        type="range",
        presets=[
            {
                "value": [
                    (today - timedelta(days=2)).isoformat(),
                    today.isoformat(),
                ],
                "label": "Last two days",
            },
            {
                "value": [
                    (today - timedelta(days=7)).isoformat(),
                    today.isoformat(),
                ],
                "label": "Last 7 days",
            },
            {
                "value": [
                    today.replace(day=1).isoformat(),
                    today.isoformat(),
                ],
                "label": "This month",
            },
            {
                "value": [
                    (today - relativedelta(months=1)).replace(day=1).isoformat(),
                    (today.replace(day=1) - timedelta(days=1)).isoformat(),
                ],
                "label": "Last month",
            },
            {
                "value": [
                    date(today.year - 1, 1, 1).isoformat(),
                    date(today.year - 1, 12, 31).isoformat(),
                ],
                "label": "Last year",
            },
        ],
    )
)