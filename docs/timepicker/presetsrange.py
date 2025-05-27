import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.TimePicker(
    label="Enter a time",
    format="12h",
    withDropdown=True,
    timeRangePresets={"startTime": "06:00:00", "endTime": "18:00:00", "interval": "01:30:00"}
)

