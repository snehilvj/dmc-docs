import dash_mantine_components as dmc

from lib.configurator import Configurator
from .data import data

target = dmc.FunnelChart(
    data=data,
    labelsPosition="right",
    withLabels=True
)

configurator = Configurator(target)
configurator.add_segmented_control("labelsPosition",data=["right", "left", "inside"], value="right")


component = configurator.panel
