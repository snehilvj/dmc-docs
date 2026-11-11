import dash_mantine_components as dmc
from .data import events

component = dmc.Schedule(
    events=events,
    dayViewProps={
        "startTime": "08:00:00",
        "endTime": "18:00:00",
        "intervalMinutes": 30,
    },
    weekViewProps={
        "startTime": "08:00:00",
        "endTime": "18:00:00",
        "withWeekendDays": False,
    },
    monthViewProps={
        "withWeekNumbers": True,
        "firstDayOfWeek": 0,
    },
    yearViewProps={
        "withWeekNumbers": True,
    },
)
