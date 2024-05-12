import dash_mantine_components as dmc
from .data import data

from lib.configurator import Configurator

target = dmc.DonutChart(
    data=data,
    withLabels=True,
    withLabelsLine=True
)

configurator = Configurator(target)

configurator.add_switch("withLabelsLine", True)

component = configurator.panel
