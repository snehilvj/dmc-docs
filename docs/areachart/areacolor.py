import dash_mantine_components as dmc
from .data import data
from lib.configurator import Configurator


target = dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    withGradient=True,
    series=[{"name": "Apples", "color": "orange.7"}],
)

configurator = Configurator(target)

configurator.add_switch("withGradient", True)

component = configurator.panel
