import dash_mantine_components as dmc
import datetime

component = dmc.Group(
    children=[
        dmc.TimeInput(label="What time is it now?"),
        dmc.TimeInput(
            label="What time is now?", format="12", value=datetime.datetime.now()
        ),
        dmc.TimeInput(
            label="What time is now?", withSeconds=True, value=datetime.datetime.now()
        ),
    ]
)
