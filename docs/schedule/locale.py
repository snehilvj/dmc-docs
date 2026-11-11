import dash_mantine_components as dmc
from .data import events

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.11.18/dayjs.min.js",  # dayjs
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.11.18/locale/fr.min.js",  # french locale
]

#app = Dash(external_scripts=scripts)

component = dmc.DatesProvider(
    dmc.Schedule(
        events=events,
        labels={
            "day": "Jour",
            "week": "Semaine",
            "month": "Mois",
            "year": "Année",
            "allDay": "Toute la journée",
            "weekday": "Jour de la semaine",
            "timeSlot": "Créneau horaire",
            "today": "Aujourd'hui",
            "previous": "Précédent",
            "next": "Suivant",
        },
    ),
    settings={"locale": "fr", "firstDayOfWeek": 0, "weekendDays": [0]},
)

