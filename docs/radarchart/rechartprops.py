import dash_mantine_components as dmc


data = [
    {"product": "Apples", "sales_january": 12000, "sales_february": 10000},
    {"product": "Oranges", "sales_january": 9800, "sales_february": 9000},
    {"product": "Tomatoes", "sales_january": 8600, "sales_february": 7000},
    {"product": "Grapes", "sales_january": 9900, "sales_february": 8000},
    {"product": "Bananas", "sales_january": 8500, "sales_february": 12000},
    {"product": "Lemons", "sales_january": 6500, "sales_february": 15000},
]

component = dmc.RadarChart(
    h=300,
    data=data,
    dataKey="product",
    withPolarRadiusAxis=True,
    polarRadiusAxisProps={"angle": 30, "tickFormatter": {"function": "formatNumberIntl"}},
    series=[
        {"name": "sales_january", "color": "lime.4", "opacity": 0.1},
        {"name": "sales_february", "color": "cyan.4", "opacity": 0.1},
    ],
)
