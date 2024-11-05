import dash_mantine_components as dmc
from .data import data

component = dmc.Stack(
    [

        dmc.Text("Apples sales:", mb="md", pl="md"),
        dmc.CompositeChart(
            h=180,
            data=data,
            dataKey="date",
            series=[{"name": "Apples", "color": "indigo.6", "type": "area"}],
            composedChartProps={"syncId": "groceries"}
        ),
        dmc.Text("Tomatoes sales:", mb="md", pl="md", mt="xl"),
        dmc.CompositeChart(
            h=180,
            data=data,
            dataKey="date",
            series=[{"name": "Tomatoes", "color": "cyan.6", "type": "bar"}],
            composedChartProps={"syncId": "groceries"}
        )
    ]
)
