import dash_mantine_components as dmc
from .data import data

from utils.configurator import Configurator

target = dmc.DonutChart(data=data, withLabels=True, withLabelsLine=True)

configurator = Configurator(target)

configurator.add_switch("withLabelsLine", True)
configurator.add_segmented_control("labelsType", ["value", "percent", "name"], "value")

component = configurator.panel
