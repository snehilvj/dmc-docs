import dash_mantine_components as dmc

data = [
  {"product": "Apples", "sales": 120},
  {"product": "Oranges", "sales": 98},
  {"product": "Tomatoes", "sales": 86},
  {"product": "Grapes", "sales": 99},
  {"product": "Bananas", "sales": 85},
  {"product": "Lemons", "sales": 65}
]


component = dmc.RadarChart(
    h=300,
    data=data,
    dataKey="product",
    withPolarRadiusAxis=True,
    series=[{ "name": "sales", "color": "blue.4", "opacity": 0.2 }]
)
