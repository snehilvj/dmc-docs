
from datetime import datetime, timedelta

today = datetime.now().date()
tomorrow = today + timedelta(days=1)

events = [
    {
        "id": 1,
        "title": "Morning Standup",
        "start": f"{today} 09:00:00",
        "end": f"{today} 09:30:00",
        "color": "blue",
    },
    {
        "id": 2,
        "title": "Team Meeting",
        "start": f"{today} 10:00:00",
        "end": f"{today} 11:30:00",
        "color": "green",
    },
    {
        "id": 3,
        "title": "Code Review",
        "start": f"{tomorrow} 14:00:00",
        "end": f"{tomorrow} 15:00:00",
        "color": "violet",
    },
    {
        "id": 4,
        "title": "All Day Conference",
        "start": f"{today} 00:00:00",
        "end": f"{tomorrow} 00:00:00",
        "color": "red",
    },
]
