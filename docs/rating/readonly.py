import dash_mantine_components as dmc

component = dmc.Group(
    children=dmc.Rating(fractions=2, value=3.5, readOnly=True),
    position="center"
)