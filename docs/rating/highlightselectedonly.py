import dash_mantine_components as dmc

component = dmc.Group(
    children=dmc.Rating( value=3, highlightSelectedOnly=True),
    position="center"
)