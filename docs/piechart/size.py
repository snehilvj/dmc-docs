import dash_mantine_components as dmc

from lib.configurator import Configurator
from .data import data

target = dmc.PieChart(
    data=data,
    size=160
)

configurator = Configurator(target)
configurator.add_number_slider("size", 275, min=80, max=300)

component = configurator.panel

