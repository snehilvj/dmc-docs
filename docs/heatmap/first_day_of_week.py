import dash_mantine_components as dmc
from .data import data

component = dmc.Heatmap(
    data=data,
    startDate="2024-02-16",
    endDate="2024-04-26",
    withWeekdayLabels=True,
    withMonthLabels=True,
    firstDayOfWeek=0,
    weekdayLabels=['', 'Mon', '', 'Wed', '', 'Fri', '']
)
