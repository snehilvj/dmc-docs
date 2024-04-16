import dash_mantine_components as dmc

component = dmc.MultiSelect(
    data=["React", "Angular", "Svelte", "Vue"],
    searchable=True,
    style={"width": 400},
)
