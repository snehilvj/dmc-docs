
from datetime import datetime
import dash_mantine_components as dmc

today = datetime.now().date()

events = [
    {
        "id": "lunch-block",
        "title": "Lunch break",
        "start": f"{today} 12:00:00",
        "end": f"{today} 13:00:00",
        "color": "gray",
        "display": "background",
    },
    {
        "id": "focus-time",
        "title": "Focus time",
        "start": f"{today} 14:00:00",
        "end": f"{today} 16:00:00",
        "color": "blue",
        "display": "background",
    },
    {
        "id": "team-meeting",
        "title": "Team meeting",
        "start": f"{today} 10:00:00",
        "end": f"{today} 11:00:00",
        "color": "violet",
    },
    {
        "id": "code-review",
        "title": "Code review",
        "start": f"{today} 14:30:00",
        "end": f"{today} 15:30:00",
        "color": "green",
    },
]

component = dmc.Schedule(
    events=events,
    date=today,
)
