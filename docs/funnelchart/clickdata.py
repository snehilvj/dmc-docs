import dash_mantine_components as dmc
from dash import Input, Output, callback
from .data import data

component = dmc.Stack(
    [
        dmc.FunnelChart(
            id="figure-funnelchart-click",
            data=data,
        ),
        dmc.Text(id="clickdata-funnelchart1"),
        dmc.Text(id="clickdata-funnelchart2"),
    ]
)

@callback(
    Output("clickdata-funnelchart1", "children"),
    Output("clickdata-funnelchart2", "children"),
    Input("figure-funnelchart-click", "clickData"),
    Input("figure-funnelchart-click", "clickSeriesName"),
)
def update(data, name):
    return f"clickData:  {data}", f"clickSeriesName: {name}"