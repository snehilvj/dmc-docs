import dash_mantine_components as dmc


from lib.configurator import Configurator

data = [
  { "month": "January", "Smartphones": 1200, "Laptops": 900, "Tablets": 200 },
  { "month": "February", "Smartphones": 1900, "Laptops": 1200, "Tablets": 400 },
  { "month": "March", "Smartphones": 400, "Laptops": 1000, "Tablets": 200 },
  { "month": "April", "Smartphones": 1000, "Laptops": 200, "Tablets": 800 },
  { "month": "May", "Smartphones": 800, "Laptops": 1400, "Tablets": 1200 },
  { "month": "June", "Smartphones": 750, "Laptops": 600, "Tablets": 1000 }
]


target = dmc.BarChart(
    h=300,
    dataKey="month",
    data=data,
    series=[
        { "name": 'Smartphones', 'color': 'violet.6' },
        { "name": 'Laptops', 'color': 'blue.6' },
        { 'name': 'Tablets', 'color': 'teal.6' },
      ],
    tickLine="y",

)

configurator = Configurator(target)

configurator.add_segmented_control("tickLine", ["x", "y", "xy", "none"], "xy")
configurator.add_segmented_control("gridAxis", ["x", "y", "xy", "none"], "x")
configurator.add_switch("withXAxis", True)
configurator.add_switch("withYAxis", True)



component = configurator.panel

