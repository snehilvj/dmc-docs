import dash_mantine_components as dmc
from dash import html

data = [
  { "name": "USA", "value": 400, "color": "indigo.6" },
  { "name": "India", "value": 300, "color": "yellow.6" },
  { "name": "Japan", "value": 100, "color": "teal.6" },
  { "name": "Other", "value": 200, "color": "gray.6" }
]

component = dmc.Group(
  [
    html.Div([
      dmc.Text("Data only for hovered segment", fz="xs", mb="sm", ta="center"),
      dmc.DonutChart(
        data=data,
        withTooltip=True,
        tooltipDataSource="segment",
        mx="auto",
      ),
    ]),
    html.Div([
      dmc.Text("Data only for all segments", fz="xs", mb="sm", ta="center"),
      dmc.DonutChart(
        data=data,
        withTooltip=True,
        mx="auto",
      )
    ])
  ],
  gap=50
)
