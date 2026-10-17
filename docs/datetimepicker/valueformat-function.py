import dash_mantine_components as dmc


# Add dayjs as external script to make it available to the function
# app = Dash(external_scripts=["https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js"])


component = dmc.DateTimePicker(
    label="Pick date and time",
    valueFormat={"function": "formatDateTimePicker"},
    value="2026-10-14 14:45:00"
)
