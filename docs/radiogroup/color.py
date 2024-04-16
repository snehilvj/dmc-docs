import dash_mantine_components as dmc

data = [
    ["react", "React", "blue"],
    ["ng", "Angular", "orange"],
    ["svelte", "Svelte", "red"],
    ["dash", "Dash", "green"],
]

component = dmc.RadioGroup(
    children=dmc.Stack([dmc.Radio(l, value=k, color=c) for k, l, c in data]),
    value="ng",
    size="sm",
)
