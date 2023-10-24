import dash_mantine_components as dmc

component = dmc.Group([dmc.Burger(size=s) for s in ["xs", "sm", "md", "lg", "xl"]])
