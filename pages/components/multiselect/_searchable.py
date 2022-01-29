import dash_mantine_components as dmc

component = dmc.MultiSelect(
    data=["React", "Angular", "Svelte", "Vue"],
    searchable=True,
    nothingFound="No options found",
    style={"width": 400},
)
