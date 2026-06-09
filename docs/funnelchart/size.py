import dash_mantine_components as dmc

from lib.configurator import Configurator
from .data import data

target = dmc.FunnelChart(
    data=data,
    size=160,
)

configurator = Configurator(target)
configurator.add_number_slider("size", min=80, max=300, value=160)


component = configurator.panel
