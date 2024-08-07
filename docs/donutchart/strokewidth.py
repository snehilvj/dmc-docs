import dash_mantine_components as dmc
from .data import data

from lib.configurator import Configurator

target = dmc.DonutChart(
    data=data,
)

configurator = Configurator(target)

configurator.add_number_slider("strokeWidth", 0, min=0, max=5)

component = configurator.panel
