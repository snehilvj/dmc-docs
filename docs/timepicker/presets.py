import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.TimePicker(
    label="Enter a time",
    format="12h",
    withDropdown=True,
    presets=['11:30', '15:45', '18:00', '20:15', '22:30']
)

