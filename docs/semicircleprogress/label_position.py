import dash_mantine_components as dmc

component = dmc.Stack([
    dmc.SemiCircleProgress( value=30, label="Bottom", mb="xl"),
    dmc.SemiCircleProgress(value=30, label="Center", labelPosition="center")
])

