from datetime import datetime

import dash_mantine_components as dmc

component = dmc.DateTimePicker(
    value=datetime.now(),
    label="Pick date and time",
    placeholder="Pick Date and time",
    timePickerProps={
        "withDropdown": True,
        "popoverProps": { "withinPortal": False },
        "format": '12h',
      }
)
