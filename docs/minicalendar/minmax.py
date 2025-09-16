import dash_mantine_components as dmc

component = dmc.MiniCalendar(
    numberOfDays=6,
    defaultDate="2025-04-13",
    minDate = "2025-04-14",
    maxDate = "2025-04-24",
)