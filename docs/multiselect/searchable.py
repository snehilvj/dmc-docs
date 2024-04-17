import dash_mantine_components as dmc

component = dmc.MultiSelect(
    data=["React", "Angular", "Svelte", "Vue"],
    searchable=True,
    w=400,
    nothingFoundMessage="Nothing Found!",
)
