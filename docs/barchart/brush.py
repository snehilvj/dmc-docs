import dash_mantine_components as dmc
from dash import callback, Input, Output
from .data import data2

component = dmc.Stack([
    dmc.BarChart(
        h=300,
        data=data2,
        dataKey="month",
        withBrush=True,
        series=[
            {"name": "Smartphones", "color": "violet.6"},
            {"name": "Laptops", "color": "blue.6"},
        ],
        id="barchart-brush",
    ),
    dmc.Text(id="barchart-brush-dragend"),
])

@callback(
    Output("barchart-brush-dragend", "children"),
    Input("barchart-brush", "brushDragEnd"),
)
def update_brush_range(brush_drag_end):
    return f"Brush range selected: {brush_drag_end}"