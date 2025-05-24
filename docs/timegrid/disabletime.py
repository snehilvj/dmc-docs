import dash_mantine_components as dmc

component = dmc.TimeGrid(
    timeRangeData={"startTime": "09:00", "endTime": "11:45", "interval": "00:15"},
    disableTime = ['10:45', '11:00', '11:30']
)
