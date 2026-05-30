from dash import Input, Output, callback
import dash_mantine_components as dmc
from .data import data


component = dmc.Box([
        dmc.Heatmap(
        id="heatmap",
        data=data,
        startDate="2024-02-16",
        endDate="2025-02-16"
    ),
    dmc.Text(id="heatmap-hoverdata"),
    dmc.Text(id="heatmap-clickdata")
])


@callback(
  Output("heatmap-clickdata", "children"),
  Input("heatmap", "clickData")
)
def update_clickdata(clickData):
    print(str(clickData))
    return f"You clicked on: {clickData}"


@callback(
  Output("heatmap-hoverdata", "children"),
  Input("heatmap", "hoverData")
)
def update_hoverdata(hoverData):
  return f"You hovered over: {hoverData}"

