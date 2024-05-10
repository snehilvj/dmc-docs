import dash_mantine_components as dmc

from lib.configurator import Configurator

data = [
  {"date": "Mar 22", "Apples": 110},
  {"date": "Mar 23", "Apples": 60},
  {"date": "Mar 24", "Apples": -80},
  {"date": "Mar 25", "Apples": 40},
  {"date": "Mar 26", "Apples": 60},
  {"date": "Mar 27", "Apples": 80}
]

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

