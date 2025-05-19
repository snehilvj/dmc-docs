import dash_mantine_components as dmc
import random

rows = [
    [
        i + 1,
        f"S-{1000 + i}",
        round(random.uniform(15, 30), 1),   # Temperature °C
        round(random.uniform(30, 70), 1),   # Humidity %
    ]
    for i in range(50)
]

component = dmc.TableScrollContainer(
    dmc.Table(
        data={
            "caption": "Synthetic Sensor Readings",
            "head": ["#", "Sensor ID", "Temperature (°C)", "Humidity (%)"],
            "body": rows,
        },
        striped=True,
        highlightOnHover=True,
        withTableBorder=True,
    ),
    maxHeight=300,
    minWidth=600,
    type="scrollarea",
)
