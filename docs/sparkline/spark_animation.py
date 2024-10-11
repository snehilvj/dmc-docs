import dash_mantine_components as dmc
from dash import  callback, Input, Output

component = dmc.Box([
    dmc.Button("Update Chart", id="btn-spark-animation", n_clicks=0),
    dmc.Sparkline(w=200, h=60, data=[], areaProps={"isAnimationActive":True}, id="spark-animation")
])


@callback(
    Output("spark-animation", "data"),
    Input("btn-spark-animation", "n_clicks")
)
def update(n):
    if n % 2 == 0:
        return [10, 20, 40, 20, 40, 10, 50]
    return [50, 10, 30, 10, 40, 50, 10]

