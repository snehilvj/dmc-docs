import dash_mantine_components as dmc

component = dmc.ChipGroup(
    [
        dmc.Chip(
            x,
            value=x,
            variant="outline",
        )
        for x in ["React", "Django", "Dash", "Vue"]
    ],
    id="chips-values",
    value=["React", "Dash"],
    multiple=True,
)
