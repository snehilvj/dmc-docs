import dash_mantine_components as dmc

component = dmc.Tooltip(
    label="chip tooltip",
    children=dmc.Chip("chip with tooltip", checked=True),
)
