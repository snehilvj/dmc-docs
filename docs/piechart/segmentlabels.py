import dash_mantine_components as dmc
from lib.configurator import Configurator
from .data import data

target = dmc.PieChart(data=data, withLabels=True)

configurator = Configurator(target)

configurator.add_switch("withLabelsLine", True)
configurator.add_segmented_control("labelsPosition", ["inside", "outside"], "outside")
configurator.add_segmented_control("labelsType", ["value", "percent"], "value")

component = configurator.panel
