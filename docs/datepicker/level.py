import dash_mantine_components as dmc

component = dmc.Group([
    dmc.DatePicker(level="decade"),
    dmc.DatePicker(level="year")
], justify="center")

