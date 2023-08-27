import dash_mantine_components as dmc

data = [
    ["react", "React", "blue"],
    ["ng", "Angular", "orange"],
    ["svelte", "Svelte", "red"],
    ["vue", "Vue", "green"],
]

component = dmc.RadioGroup(
    [dmc.Radio(l, value=k, color=c) for k, l, c in data],
    value="ng",
    size="sm",
)
