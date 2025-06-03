
import dash_mantine_components as dmc

component = dmc.Center(
    dmc.DatePicker(
        value="2024-11-08",
        defaultDate="2024-11-01",
        disabledDates={"function": "excludeDate"},
        m="lg"
    )
)