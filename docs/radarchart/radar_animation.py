from random import randint
import dash_mantine_components as dmc
from dash import  callback, Input, Output

component = dmc.Box([
    dmc.Button("Update Chart", id="btn-radarchart-animation"),
    dmc.RadarChart(
        id="radarchart-animation",
        h=300,
        data=[{}],
        dataKey="product",
        withPolarRadiusAxis=True,
        radarProps={"isAnimationActive": True,},
        series=[{"name": "sales", "color": "blue.4", "opacity": 0.2}],
    )
])


@callback(
    Output("radarchart-animation", "data"),
    Input("btn-radarchart-animation", "n_clicks")
)
def update(n):
    return  [
    {"product": "Apples", "sales": randint(20, 100)},
    {"product": "Oranges", "sales": randint(20, 100)},
    {"product": "Tomatoes", "sales": randint(20, 100)},
    {"product": "Grapes", "sales": randint(20, 100)},
    {"product": "Bananas", "sales": randint(20, 100)},
    {"product": "Lemons", "sales": randint(20, 100)},
]

