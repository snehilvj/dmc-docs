import dash_mantine_components as dmc

component = dmc.MultiSelect(
    data=["React", "Angular", "Svelte", "Vue"],
    value=["Vue", "Angular"],
    clearable=True,
    style={"width": 400},
)
