from random import randint
import dash_mantine_components as dmc
from dash import  callback, Input, Output

component = dmc.Box([
    dmc.Button("Update Chart", id="btn-piechart-animation", n_clicks=0),
    dmc.PieChart(
        id="piechart-animation",
        data=[{}],
        pieProps={"isAnimationActive":True},
    ),
])


@callback(
    Output("piechart-animation", "data"),
    Input("btn-piechart-animation", "n_clicks")
)
def update(n):
    return   [
      { "name": "USA", "value": randint(10, 400), "color": "indigo.6" },
      { "name": "India", "value": randint(10, 400), "color": "yellow.6" },
      { "name": "Japan", "value": randint(10, 400), "color": "teal.6" },
      { "name": "Other", "value": randint(10, 400), "color": "gray.6" }
    ]


