import dash_mantine_components as dmc

component = dmc.ChipGroup(
    [dmc.Chip(x, value=x) for x in ["React", "Django", "Dash", "Vue"]],
    value="React",
)
