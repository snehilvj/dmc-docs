import dash_mantine_components as dmc

component = dmc.Select(
    data=["React", "Angular", "Svelte", "Vue"],
    value="Vue",
    clearable=True,
    style={"width": 200},
)