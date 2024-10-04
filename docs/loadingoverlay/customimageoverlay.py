
import dash_mantine_components as dmc
import random

# Generate random data for the BarChart
data = [
    {
        "month": month,
        "Smartphones": random.randint(50, 300),
        "Laptops": random.randint(30, 200),
        "Tablets": random.randint(20, 150),
    }
    for month in ["January", "February", "March", "April", "May", "June"]
]

component = dmc.Box(
    children=[
        dmc.Stack(
            pos="relative",
            p=10,
            children=[
                dmc.LoadingOverlay(
                    visible=True,
                    id="custom-loading-overlay",
                    zIndex=10,
                    loaderProps={
                        "variant": "custom",
                        "children": dmc.Image(
                            radius="md",
                            src="/assets/custom_loadingoverlay.gif",
                        )
                    },
                    overlayProps={"radius": "sm", "blur": 2},
                ),
                dmc.BarChart(
                    h=300,
                    dataKey="month",
                    data=data,
                    type="stacked",
                    series=[
                        {"name": "Smartphones", "color": "violet.6"},
                        {"name": "Laptops", "color": "blue.6"},
                        {"name": "Tablets", "color": "teal.6"},
                    ],
                ),
            ],
        ),
    ]
)

