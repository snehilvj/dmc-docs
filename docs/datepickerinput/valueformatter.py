import dash_mantine_components as dmc

component = dmc.DatePickerInput(
    label="Pick multiple dates",
    type="multiple",
    placeholder="Pick multiple dates",
    clearable=True,
    valueFormatter={"function": "formatDatesSelected"},
),