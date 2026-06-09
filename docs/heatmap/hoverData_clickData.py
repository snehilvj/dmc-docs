from dash import Input, Output, callback
import dash_mantine_components as dmc
from .data import data


component = dmc.Box([
        dmc.Heatmap(
        id="heatmap-chart",
        data=data,
        startDate="2024-02-16",
        endDate="2025-02-16"
    ),
    dmc.Text(id="heatmap-clickdata"),
    dmc.Text(id="heatmap-hoverdata")
])


@callback(
  Output("heatmap-clickdata", "children"),
  Input("heatmap-chart", "clickData")
)
def update_clickdata(clickData):
    return f"You clicked on: {clickData}"


@callback(
  Output("heatmap-hoverdata", "children"),
  Input("heatmap-chart", "hoverData")
)
def update_hoverdata(hoverData):
  return f"You hovered over: {hoverData}"

