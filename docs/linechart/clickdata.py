from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.LineChart(
            id="figure-linechart",
            h=300,
            dataKey="date",
            data=data,
            withLegend=True,
            series=[
                { "name": 'Apples', 'color': 'indigo.6' },
                { "name": 'Oranges', 'color': 'blue.6' },
                { 'name': 'Tomatoes', 'color': 'teal.6' },
              ],
        ),
        dmc.Text(id="clickdata-linechart"),
    ]
)

@callback(
    Output("clickdata-linechart", "children"),
    Input("figure-linechart", "clickData"),
)
def update(clickdata):
    return str(clickdata)



