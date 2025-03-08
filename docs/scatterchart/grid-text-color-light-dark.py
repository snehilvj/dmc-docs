import dash_mantine_components as dmc

from .data import data1

component = dmc.ScatterChart(
    h=300,
    data=data1,
    dataKey={"x": "age", "y": "BMI"},
    tickLine="xy",
    xAxisLabel="Age",
    yAxisLabel="BMI",
    className="chart-grid-text-colors",
)
