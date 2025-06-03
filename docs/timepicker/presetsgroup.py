import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.TimePicker(
    label="Enter a time",
    withDropdown=True,
    maxDropdownContentHeight=300,
    presets = [
        {"label": 'Morning', "values": ['06:00:00', '08:00:00', '10:00:00']},
        {"label": 'Afternoon', "values": ['12:00:00', '14:00:00', '16:00:00']},
        {"label": 'Evening', "values": ['18:00:00', '20:00:00', '22:00:00']},
    ],
    mb=120,
)

