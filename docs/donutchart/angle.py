import dash_mantine_components as dmc
from .data import data

component = dmc.DonutChart(
  data=data,
  startAngle=180,
  endAngle=0
)
