import dash_mantine_components as dmc
from .data import data

from lib.configurator import Configurator

target = dmc.Heatmap(
    data=data,
    startDate="2024-02-16",
    endDate="2024-04-16",
    withWeekdayLabels=True,
     withMonthLabels=True,
    rectSize=10,
    rectRadius=2,
    gap=1
)

configurator = Configurator(target)

configurator.add_number_slider("rectSize", 10, min=6, max=20)
configurator.add_number_slider("rectRadius", 2, min=0, max=20)
configurator.add_number_slider("gap", 1, min=0, max=5)

component = configurator.panel
