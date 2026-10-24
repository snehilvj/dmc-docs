import dash_mantine_components as dmc
from dash import callback, Input, Output
from .data import data2

component = dmc.Stack([
    dmc.LineChart(
        h=300,
        data=data2,
        dataKey="month",
        withBrush=True,
        series=[
            {"name": "Smartphones", "color": "violet.6"},
            {"name": "Laptops", "color": "blue.6"},
        ],
        id="linechart-brush",
    ),
    dmc.Text(id="linechart-brush-dragend"),
])

@callback(
    Output("linechart-brush-dragend", "children"),
    Input("linechart-brush", "brushDragEnd"),
)
def update_brush_range(brush_drag_end):
    return f"Brush range selected: {brush_drag_end}"