from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.BarChart(
            id="figure-barchart-hover",
            h=300,
            dataKey="month",
            data=data,
            type="stacked",
            series=[
                {"name": "Smartphones", "color": "violet.6"},
                {"name": "Laptops", "color": "blue.6"},
                {"name": "Tablets", "color": "teal.6"},
            ],
            withLegend=True,
            withTooltip=False,
        ),
        dmc.Text(id="hoverdata-barchart1"),
        dmc.Text(id="hoverdata-barchart2"),
    ]
)

@callback(
    Output("hoverdata-barchart1", "children"),
    Output("hoverdata-barchart2", "children"),
    Input("figure-barchart-hover", "hoverData"),
    Input("figure-barchart-hover", "hoverSeriesName"),
)
def update(data, name):
    return f"hoverData:  {data}", f"hoverSeriesName: {name}"

