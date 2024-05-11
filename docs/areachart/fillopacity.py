
import dash_mantine_components as dmc
from .data import data
from lib.configurator import Configurator

target = dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"}
    ],
    fillOpacity="0.2"
)

configurator = Configurator(target)


configurator.add_segmented_control("type", ["default", "stacked"], "default")
configurator.add_number_slider("fillOpacity", 0.2, min=0, max=1)
configurator.add_switch("withGradient", True)


component = configurator.panel



