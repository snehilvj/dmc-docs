import dash_mantine_components as dmc
import datetime

component = dmc.Group(
    gap=50,
    children=[
        dmc.TimeInput(label="What time is it now?"),
        dmc.TimeInput(
            label="What time is it now?",
            withSeconds=True,
            value="23:15:45",
        ),
    ],
)
