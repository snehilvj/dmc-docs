from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data


component = dmc.Group(
    [
        dmc.AreaChart(
            id="areachart",
            h=300,
            dataKey="date",
            data=data,
            type="stacked",
            series=[
                {"name": "Apples", "color": "indigo.6"},
                {"name": "Oranges", "color": "blue.6"},
                {"name": "Tomatoes", "color": "teal.6"}
            ]
        ),
        dmc.Text(id="clickdata-areachart"),
    ]
)

@callback(
    Output("clickdata-areachart", "children"),
    Input("areachart", "clickData"),
)
def update(clickdata):
    return str(clickdata)



