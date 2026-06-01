import dash_mantine_components as dmc
from dash import Input, Output, callback
from .data import data

component = dmc.Stack(
    [
        dmc.FunnelChart(
            id="figure-funnelchart",
            data=data,
        ),
        dmc.Text(id="hoverdata-funnelchart1"),
        dmc.Text(id="hoverdata-funnelchart2"),
    ]
)

@callback(
    Output("hoverdata-funnelchart1", "children"),
    Output("hoverdata-funnelchart2", "children"),
    Input("figure-funnelchart", "hoverData"),
    Input("figure-funnelchart", "hoverSeriesName"),
)
def update(data, name):
    return f"hoverData:  {data}", f"hoverSeriesName: {name}"