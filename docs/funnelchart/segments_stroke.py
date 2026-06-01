import dash_mantine_components as dmc

from lib.configurator import Configurator
from .data import data

target = dmc.FunnelChart(
    data=data,
    strokeWidth=1
)

configurator = Configurator(target)
configurator.add_number_slider("strokeWidth", min=0, max=5, value=1)


component = configurator.panel
