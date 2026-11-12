from datetime import datetime, timedelta
import dash_mantine_components as dmc

today = datetime.now().date()
tomorrow = today + timedelta(days=1)
week_start = today - timedelta(days=today.weekday())

events = [
    {
        "id": "standup",
        "title": "Morning Standup",
        "start": f"{today} 09:00:00",
        "end": f"{today} 09:30:00",
        "color": "blue",
    },
    {
        "id": "team-meeting",
        "title": "Team Meeting",
        "start": f"{today} 10:00:00",
        "end": f"{today} 11:30:00",
        "color": "green",
    },
    {
        "id": "code-review",
        "title": "Code Review",
        "start": f"{tomorrow} 14:00:00",
        "end": f"{tomorrow} 15:00:00",
        "color": "violet",
    },
    {
        "id": "weekly-review-series",
        "title": "Weekly review",
        "start": f"{week_start} 16:00:00",
        "end": f"{week_start} 17:00:00",
        "color": "orange",
        "recurrence": {
            "rrule": "FREQ=WEEKLY;COUNT=8",
        },
    },
]

component = dmc.Schedule(
    events=events,
    withAgenda=True,
)