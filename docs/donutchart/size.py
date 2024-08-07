import dash_mantine_components as dmc
from .data import data

from lib.configurator import Configurator

target = dmc.DonutChart(data=data, size=160, thickness=20)

configurator = Configurator(target)
configurator.add_number_slider("size", 275, min=80, max=300)
configurator.add_number_slider("thickness", 20, min=2, max=30)

component = configurator.panel
