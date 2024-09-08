import dash_mantine_components as dmc

component = dmc.MonthPickerInput(
    disabled=True,
    valueFormat="YYYY MMM",
    type="multiple",
    label="Pick month (Disabled)",
    placeholder="Pick month",
)
