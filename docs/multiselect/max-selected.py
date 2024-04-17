import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Select frameworks",
    description="You can select a maximum of 3 frameworks.",
    data=["React", "Angular", "Svelte", "Vue"],
    maxValues=3,
    w=400,
)
