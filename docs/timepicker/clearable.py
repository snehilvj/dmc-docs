import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.TimePicker(
    label="Enter a time",
    withDropdown=True,
    withSeconds=True,
    clearable=True,
    value="12:30:00"
)

