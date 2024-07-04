import dash_mantine_components as dmc
from lib.configurator import Configurator
from .data import data

target = dmc.PieChart(
    data=data,
    strokeWidth=1
)

configurator = Configurator(target)
configurator.add_number_slider("strokeWidth", 1, min=0, max=2)

component = configurator.panel
