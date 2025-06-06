
import dash_mantine_components as dmc

# makes dayjs available
#app = Dash(exteral_scripts=["https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js"])

component = dmc.Center(
    dmc.DatePicker(
        value="2024-11-08",
        defaultDate="2024-11-01",
        disabledDates={"function": "excludeDate"},
        m="lg"
    )
)