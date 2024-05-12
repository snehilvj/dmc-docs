import dash_mantine_components as dmc
from .data import data
from lib.configurator import Configurator

target = dmc.PieChart(
    data=data,
)

configurator = Configurator(target)


configurator.add_switch("withLabels", True)
configurator.add_switch("withLabelsLine", False)
configurator.add_segmented_control("labelsPosition", ["inside", "outside"], "outside")
configurator.add_segmented_control("labelsType", ["value", "percent"], "value")
configurator.add_number_slider("size", 160, min=80, max=300)
configurator.add_number_slider("strokeWidth", 0, min=0, max=5)

component = configurator.panel

