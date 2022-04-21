import dash_mantine_components as dmc

component = dmc.Chips(
    data=[{"label": x, "value": x} for x in ["React", "Django", "Dash", "Vue"]],
    value=["React", "Dash"],
    multiple=True,
)
