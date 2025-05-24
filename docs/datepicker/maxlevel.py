import dash_mantine_components as dmc

component = dmc.Group([
    dmc.DatePicker(maxLevel="year"),
    dmc.DatePicker(maxLevel="month")
], justify="center", gap="xl")

