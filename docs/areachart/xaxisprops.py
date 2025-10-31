
import dash_mantine_components as dmc
from dash import Dash
from datetime import datetime

data = [
  {"date": datetime(2025, 3, 22), "Apples": 2890, "Oranges": 2338, "Tomatoes": 2452},
  {"date": datetime(2025, 3, 23), "Apples": 2756, "Oranges": 2103, "Tomatoes": 2402},
  {"date": datetime(2025, 3, 24), "Apples": 3322, "Oranges": 986, "Tomatoes": 1821},
  {"date": datetime(2025, 3, 25), "Apples": 3470, "Oranges": 2108, "Tomatoes": 2809},
  {"date": datetime(2025, 3, 26), "Apples": 3129, "Oranges": 1726, "Tomatoes": 2290}
]

component = dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    series = [
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"}
    ],
    curveType="linear",
    tickLine="xy",
    withGradient=False,
    withDots=False,
    xAxisProps={"tickFormatter": {"function": "formatDatetime"}},
    valueFormatter={"function": "formatNumberIntl"},
)
