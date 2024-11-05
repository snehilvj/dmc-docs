import dash_mantine_components as dmc
from .data import data
from lib.configurator import Configurator

target = dmc.CompositeChart(
    h=300,
    data=data,
    dataKey="date",
    strokeWidth=2,
    maxBarWidth=30,
    series=[
        {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
        {"name": "Apples", "color": "red.8", "type": "line"},
        {"name": "Oranges", "color": "yellow.8", "type": "area"},
    ]
)

configurator = Configurator(target)

configurator.add_number_slider("strokeWidth", 2, min=0.5, max=5)

component = configurator.panel
