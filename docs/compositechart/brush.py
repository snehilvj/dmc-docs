import dash_mantine_components as dmc
from dash import callback, Input, Output
from .data import data2

component = dmc.Stack([
    dmc.CompositeChart(
        h=300,
        data=data2,
        dataKey="date",
        maxBarWidth=30,
        withBrush=True,
        series=[
            {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
            {"name": "Apples", "color": "red.8", "type": "line"},
            {"name": "Oranges", "color": "yellow.8", "type": "area"},
        ],
        id="compositechart-brush",
    ),
    dmc.Text(id="compositechart-brush-dragend"),
])


@callback(
    Output("compositechart-brush-dragend", "children"),
    Input("compositechart-brush", "brushDragEnd"),
)
def update_brush_range(brush_drag_end):
    return f"Brush range selected: {brush_drag_end}"