from random import randint
import dash_mantine_components as dmc
from dash import  callback, Input, Output

component = dmc.Box([
    dmc.Button("Update Date", id="btn-linechart-animation"),
    dmc.LineChart(
        id="linechart-animation",
        h=300,
        dataKey="date",
        data=[{}],
        tooltipAnimationDuration=500,
        lineProps={"isAnimationActive":True,
                        "animationDuration": 500,
                        "animationEasing": "ease-in-out",
                        "animationBegin": 500},
        series=[
            {"name": "Apples", "color": "indigo.6"},
            {"name": "Oranges", "color": "blue.6"},
            {"name": "Tomatoes", "color": "teal.6"},
        ],
    )
])


@callback(
    Output("linechart-animation", "data"),
    Input("btn-linechart-animation", "n_clicks")
)
def update(n):
    return [
    {"date": "Mar 22", "Apples": 2890, "Oranges": 2338, "Tomatoes": randint(1000, 4000)},
    {"date": "Mar 23", "Apples": 2756, "Oranges": 2103, "Tomatoes": randint(1000, 4000)},
    {"date": "Mar 24", "Apples": 3322, "Oranges": 986, "Tomatoes": randint(1000, 4000)},
    {"date": "Mar 25", "Apples": 3470, "Oranges": 2108, "Tomatoes": randint(1000, 4000)},
    {"date": "Mar 26", "Apples": 3129, "Oranges": 1726, "Tomatoes": randint(1000, 4000)}
]

