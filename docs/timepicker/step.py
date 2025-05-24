import dash_mantine_components as dmc

component =  dmc.TimePicker(
    label="Enter a time",
    withSeconds=True,
    withDropdown=True,
    hoursStep=1,
    minutesStep=5,
    secondsStep=10
)
