from random import randint

import dash
import dash_mantine_components as dmc
from dash import callback, Input, Output

component = dmc.Box(
    [
        dmc.Button("Update Chart", id="btn-barchart-animation"),
        dmc.BarChart(
            id="barchart-animation",
            h=300,
            dataKey="month",
            data=[{}],
            type="stacked",
            barProps={"isAnimationActive": True},
            series=[
                {"name": "Smartphones", "color": "violet.6"},
                {"name": "Laptops", "color": "blue.6"},
                {"name": "Tablets", "color": "teal.6"},
            ],
        ),
    ]
)


@callback(
    Output("barchart-animation", "data"), Input("btn-barchart-animation", "n_clicks")
)
def update(n):
    if n and n > 0:
        return [
            {
                "month": month,
                "Smartphones": randint(50, 300),
                "Laptops": randint(30, 200),
                "Tablets": randint(20, 150),
            }
            for month in ["January", "February", "March", "April", "May", "June"]
        ]
    return dash.no_update
