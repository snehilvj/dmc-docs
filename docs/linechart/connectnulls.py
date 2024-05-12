import dash_mantine_components as dmc

from lib.configurator import Configurator


data = [
  {"date": "Mar 22", "Apples": 110},
  {"date": "Mar 23", "Apples": 60},
  {"date": "Mar 24", "Apples": -80},
  {"date": "Mar 25", "Apples": 40},
  {"date": "Mar 26", "Apples": None},
  {"date": "Mar 27", "Apples": 80}
]

target = dmc.LineChart(
    h=300,
    dataKey="date",
    data=data,
    connectNulls=True,
    series=[{"name": "Apples", "color": "indigo.6"}],
    curveType="linear",
)

configurator = Configurator(target)

configurator.add_select(
    "curveType",
    ["Bump", "Linear", "Natural", "Monotone", "Step", "StepBefore", "StepAfter"],
    "Linear",
)
configurator.add_switch("connectNulls", True)

component = configurator.panel

