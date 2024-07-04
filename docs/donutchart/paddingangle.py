import dash_mantine_components as dmc
from .data import data

from lib.configurator import Configurator

target = dmc.DonutChart(
    data=data,
    paddingAngle=30
)

configurator = Configurator(target)
configurator.add_number_slider("paddingAngle", 30, min=0, max=30)

component = configurator.panel

