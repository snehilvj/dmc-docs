import dash_mantine_components as dmc

from lib.configurator import Configurator
from .data import data

target = dmc.BarChart(
    h=300,
    dataKey="date",
    data=data,
    fillOpacity=0.5,
    series=[{"name": "Smartphones", "color": "orange.7"}],
)

configurator = Configurator(target)

configurator.add_number_slider("fillOpacity", 0.5, min=0, max=1, step=0.1)

component = configurator.panel
