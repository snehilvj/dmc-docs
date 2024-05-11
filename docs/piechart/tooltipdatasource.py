import dash_mantine_components as dmc
from dash import html
from .data import data

component = dmc.Group(
  [
    html.Div([
      dmc.Text("Data only for hovered segment", fz="xs", mb="sm", ta="center"),
      dmc.PieChart(
        data=data,
        withTooltip=True,
        tooltipDataSource="segment",
        mx="auto",
      ),
    ]),
    html.Div([
      dmc.Text("Data only for all segments", fz="xs", mb="sm", ta="center"),
      dmc.PieChart(
        data=data,
        withTooltip=True,
        mx="auto",
      )
    ])
  ],
  gap=50
)
