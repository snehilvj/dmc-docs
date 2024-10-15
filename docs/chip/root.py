import dash_mantine_components as dmc

component = dmc.Chip(
    "Chip with props added to root",
    wrapperProps={"data-testid": "wrapper"},
    checked=True,
)
