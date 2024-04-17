import random

import dash_mantine_components as dmc


def create_graph():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
    ]
    data = [
        {
            "month": month,
            "Smartphones": random.randint(700, 1800),
            "Laptops": random.randint(100, 1000),
            "Tablets": random.randint(200, 600),
            "Watches": random.randint(200, 1800),
        }
        for month in months
    ]

    return dmc.BarChart(
        h=500,
        data=data,
        dataKey="month",
        series=[
            {"name": "Smartphones", "color": "violet.6"},
            {"name": "Laptops", "color": "blue.6"},
            {"name": "Tablets", "color": "teal.6"},
            {"name": "Watches", "color": "indigo.6"},
        ],
        tickLine="y",
    )
