import dash_mantine_components as dmc


data = [
    {"product": "Apples", "sales_january": 120, "sales_february": 100},
    {"product": "Oranges", "sales_january": 98, "sales_february": 90},
    {"product": "Tomatoes", "sales_january": 86, "sales_february": 70},
    {"product": "Grapes", "sales_january": 99, "sales_february": 80},
    {"product": "Bananas", "sales_january": 85, "sales_february": 120},
    {"product": "Lemons", "sales_january": 65, "sales_february": 150},
]

component = dmc.RadarChart(
    h=300,
    data=data,
    dataKey="product",
    withPolarRadiusAxis=True,
    polarRadiusAxisProps={"angle": 30},
    series=[
        {"name": "sales_january", "color": "lime.4", "opacity": 0.1},
        {"name": "sales_february", "color": "cyan.4", "opacity": 0.1},
    ],
)
