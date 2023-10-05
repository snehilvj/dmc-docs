import dash_mantine_components as dmc

component = dmc.Indicator(
    dmc.Button("Update", variant="outline"), inline=True, processing=True, size=20
)
