import dash_mantine_components as dmc


component = dmc.Group(
    gap=50,
    mb=60,
    children=[
        dmc.TimePicker(
            label="Enter time (24h format)",
            withSeconds=True,
            withDropdown=True
        ),
        dmc.TimePicker(
            label="Enter time (12h format)",
            withSeconds=True,
            withDropdown=True,
            format="12h"
        ),
    ],
)
