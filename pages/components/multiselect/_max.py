import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Select frameworks",
    description="You can select a maximum of 3 frameworks.",
    data=["React", "Angular", "Svelte", "Vue"],
    maxSelectedValues=3,
    style={"width": 400},
)
