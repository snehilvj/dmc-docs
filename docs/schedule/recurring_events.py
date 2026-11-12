import dash_mantine_components as dmc

events = [
    {
        "id": "schedule-series",
        "title": "Weekly planning (series)",
        "start": "2024-01-15 10:00:00",
        "end": "2024-01-15 11:00:00",
        "color": "blue",
        "recurrence": {
            "rrule": "FREQ=WEEKLY;BYDAY=MO,WE;COUNT=16",
            "exdate": ["2024-01-17 10:00:00"],
        },
    },
    {
        "id": "schedule-series-override",
        "title": "Weekly planning (moved one occurrence)",
        "start": "2024-01-17 16:00:00",
        "end": "2024-01-17 17:00:00",
        "color": "grape",
        "recurringEventId": "schedule-series",
        "recurrenceId": "2024-01-17 10:00:00",
    },
    {
        "id": "schedule-one-off",
        "title": "One-off roadmap review",
        "start": "2024-01-18 12:00:00",
        "end": "2024-01-18 13:00:00",
        "color": "green",
    },
]

component = dmc.Schedule(
     events=events,
     date='2024-01-15'
)