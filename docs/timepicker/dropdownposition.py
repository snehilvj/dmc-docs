import dash_mantine_components as dmc
from dash import callback, Input, Output


component = dmc.TimePicker(
    label="Enter a time",
    withDropdown=True,
    popoverProps={
        "position": 'top-start',
        "middlewares": {"flip": False, "shift": False },
      }
)

