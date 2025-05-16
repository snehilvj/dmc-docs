import dash_mantine_components as dmc

component =  dmc.TimePicker(
    label="Enter a time",
    format="12h",
    amPmLabels={"am": 'पूर्वाह्न', "pm": 'अपराह्न'}
)
