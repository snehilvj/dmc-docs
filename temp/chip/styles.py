import dash_mantine_components as dmc

styles = {
    "label": {
        "&[data-checked]": {
            "&, &:hover": {
                "backgroundColor": dmc.theme.DEFAULT_COLORS["indigo"][5],
                "color": "white",
            },
        },
    }
}

component = dmc.ChipGroup(
    [dmc.Chip(x, value=x, styles=styles) for x in ["React", "Django", "Dash", "Vue"]],
    multiple=True,
    value=["React", "Dash"],
)
