import dash_mantine_components as dmc

component = dmc.Select(
    data=["React", "Angular", "Svelte", "Vue"],
    searchable=True,
    nothingFound="No options found",
    style={"width": 200},
)
