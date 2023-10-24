import dash_mantine_components as dmc
import datetime

component = dmc.Group(
    spacing=50,
    children=[
        dmc.TimeInput(label="What time is it now?"),
        dmc.TimeInput(
            label="What time is it now?",
            withSeconds=True,
            value=datetime.datetime.now(),
        ),
    ],
)
