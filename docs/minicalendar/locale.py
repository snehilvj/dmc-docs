import dash_mantine_components as dmc


component = dmc.DatesProvider(
    dmc.MiniCalendar(locale="fr", defaultDate="2025-04-01"),
    settings={"locale": "fr"}
)