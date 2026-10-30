import dash_mantine_components as dmc
from .data import data3

component = dmc.ScatterChart(
    h=350,
    data=data3,
    dataKey={"x": "month", "y": "value"},
    withLegend=True,
    withRightYAxis=True,
    xAxisLabel="Month",
    yAxisLabel="Revenue",
    rightYAxisLabel="Conversion rate",
    rightYAxisProps={"unit": "%"},
)