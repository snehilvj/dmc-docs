from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.BarChart(
            id="figure-barchart",
            h=300,
            dataKey="month",
            data=data,
            type="stacked",
            series=[
                {"name": "Smartphones", "color": "violet.6"},
                {"name": "Laptops", "color": "blue.6"},
                {"name": "Tablets", "color": "teal.6"}
            ],
        ),
        dmc.Text(id="clickdata-barchart"),
    ]
)

@callback(
    Output("clickdata-barchart", "children"),
    Input("figure-barchart", "clickData"),
)
def update(clickdata):
    return str(clickdata)



