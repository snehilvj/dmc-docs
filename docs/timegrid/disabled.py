import dash_mantine_components as dmc

component = dmc.TimeGrid(
    timeRangeData={"startTime": "09:00", "endTime": "22:00", "interval": "01:00"},
    disabled=True
)
