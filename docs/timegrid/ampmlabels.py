import dash_mantine_components as dmc

component = dmc.TimeGrid(
    timeRangeData={"startTime": "09:00", "endTime": "22:00", "interval": "01:00"},
    format="12h",
    amPmLabels={"am": 'पूर्वाह्न', "pm": 'अपराह्न'}
)
