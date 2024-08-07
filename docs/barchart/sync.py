import dash_mantine_components as dmc
from .data import data

component = dmc.Stack(
    [
        dmc.Text("Smartphone sales:"),
        dmc.BarChart(
            h=180,
            dataKey="month",
            data=data,
            series=[{"name": "Smartphones", "color": "violet.6"}],
            barChartProps={"syncId": "tech"},
        ),
        dmc.Text("Laptop sales"),
        dmc.BarChart(
            h=180,
            dataKey="month",
            data=data,
            series=[{"name": "Laptops", "color": "teal.6"}],
            barChartProps={"syncId": "tech"},
        ),
    ]
)
