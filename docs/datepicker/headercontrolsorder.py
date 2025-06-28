import dash_mantine_components as dmc

component = dmc.DatePicker(
    value="2025-02-01",
    headerControlsOrder = ['level', 'previous', 'next'],
    styles = {
        "calendarHeaderLevel": {
            "justifyContent": 'flex-start',
            "paddingInlineStart": 8,
        },
    }
)