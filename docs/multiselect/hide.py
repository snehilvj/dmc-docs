import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Select frameworks",
    placeholder="Select all you like!",
    hidePickedOptions=True,
    value=["React", "Angular"],
    data=["React", "Angular", "Svelte", "Vue"],
    w=400,
    mb=140,
    dropdownOpened=True,
)
