import dash_mantine_components as dmc

component = dmc.Group([
    dmc.DatePicker(firstDayOfWeek=0),
    dmc.DatePicker(firstDayOfWeek=6)
], justify="center", gap="xl")

