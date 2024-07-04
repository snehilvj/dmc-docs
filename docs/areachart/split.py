
import dash_mantine_components as dmc

data = [
  {"date": "Mar 22", "Apples": 110},
  {"date": "Mar 23", "Apples": 60},
  {"date": "Mar 24", "Apples": -80},
  {"date": "Mar 25", "Apples": 40},
  {"date": "Mar 26", "Apples": -40},
  {"date": "Mar 27", "Apples": 80}
]

component = dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    type="split",
    series=[{ "name": 'Apples', 'color': 'indigo.6' },
        { "name": 'Oranges', 'color': 'blue.6' },
        { 'name': 'Tomatoes', 'color': 'teal.6' },
      ],
)

