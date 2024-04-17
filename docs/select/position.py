import dash_mantine_components as dmc

component = dmc.Select(
    label="Your favorite framework/library",
    data=["React", "Angular", "Svelte", "Vue"],
    value="Vue",
    clearable=True,
    comboboxProps={"position": "top"},
    w=200,
)
