import dash_mantine_components as dmc
from .data import data
from lib.configurator import Configurator

target = dmc.LineChart(
    h=300,
    dataKey="date",
    data=data,
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"},
    ],
    strokeWidth=2,
)

configurator = Configurator(target)

configurator.add_number_slider("strokeWidth", 2, min=0.5, max=5)

component = configurator.panel
