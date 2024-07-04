
import dash_mantine_components as dmc
from .data import data

component = dmc.Stack(
    [
        dmc.Text("Apples sales:"),
        dmc.AreaChart(
            h=180,
            dataKey="date",
            data=data,
            series=[{"name": "Apples", "color": "indigo.6"}],
            areaChartProps={"syncId": 'groceries' },
        ),
        dmc.Text("Tomatoes sales"),
        dmc.AreaChart(
            h=180,
            dataKey="date",
            data=data,
            series=[{"name": "Tomatoes", "color": "teal.6"}],
            areaChartProps={"syncId": 'groceries' },
        ),
    ]
)

