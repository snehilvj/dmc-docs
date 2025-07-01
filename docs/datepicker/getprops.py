
import dash_mantine_components as dmc

# Adding dayjs as external script to make it available to the function
# app = Dash(external_scripts=["https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js"])

component = dmc.DatePicker(
    defaultDate="2025-06-01",
    getDayProps={"function": "highlightFriday13"},
    getYearControlProps={"function": "yearControlProps"},
    getMonthControlProps={"function": "monthControlProps"},
    my="lg"
)
