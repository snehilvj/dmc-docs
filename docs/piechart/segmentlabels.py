import dash_mantine_components as dmc

from lib.configurator import Configurator

data = [
  { "name": "USA", "value": 400, "color": "indigo.6" },
  { "name": "India", "value": 300, "color": "yellow.6" },
  { "name": "Japan", "value": 100, "color": "teal.6" },
  { "name": "Other", "value": 200, "color": "gray.6" }
]

target = dmc.PieChart(
    data=data,
    withLabels=True
)

configurator = Configurator(target)

configurator.add_switch("withLabelsLine", False)
configurator.add_segmented_control("labelsPosition", ["inside", "outside"], "outside")
configurator.add_segmented_control("labelsType", ["value", "percent"], "value")

component = configurator.panel
