import dash_mantine_components as dmc
from .data import data

component = dmc.Heatmap(
    data=data,
    startDate="2024-02-16",
    endDate="2025-02-16",
    withWeekdayLabels=True,
    withMonthLabels=True,
    weekdayLabels=["Dim", "Lun", "", "Mer", "", "Ven", ""],
    monthLabels=[
        "Jan",
        "Fév",
        "Mar",
        "Avr",
        "Mai",
        "Jun",
        "Jul",
        "Aoû",
        "Sep",
        "Oct",
        "Nov",
        "Déc",
    ]
)
