import dash_mantine_components as dmc

component = dmc.Group(
    dmc.PinInput(oneTimeCode=True, **{"aria-label": "One Time Code"}),
    position="center"
)