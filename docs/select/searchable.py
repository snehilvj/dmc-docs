import dash_mantine_components as dmc

component = dmc.Select(
    data=["React", "Angular", "Svelte", "Vue"],
    searchable=True,
    style={"width": 200},
)
