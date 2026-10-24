import dash_mantine_components as dmc

component = dmc.MonthPickerInput(
    type="multiple",
    label="Pick multiple dates",
    placeholder="Pick multiple dates",
    valueFormatter={"function": "formatDatesSelected"}
)
