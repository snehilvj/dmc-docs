import dash_mantine_components as dmc

component = dmc.Popover(
    width=300,
    position="bottom",
    withArrow=True,
    zIndex=2000,
    shadow="md",
    children=[
        dmc.PopoverTarget(dmc.Button("Toggle Popover")),
        dmc.PopoverDropdown(
            dmc.MultiSelect(
                label="Your favorite libraries",
                placeholder="Pick values",
                data=["React", "Angular", "Vue", "Svelte"],
                comboboxProps={"withinPortal": False},
            )
        ),
    ],
)
