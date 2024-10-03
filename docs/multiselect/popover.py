import dash_mantine_components as dmc

component = dmc.Popover(
    width=300,
    position="bottom",
    withArrow=True,
    shadow="md",
    children=[
        dmc.PopoverTarget(dmc.Button("Toggle Popover")),
        dmc.PopoverDropdown(
            dmc.MultiSelect(
                label="Your favorite libraries",
                placeholder="Pick values",
                data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
                comboboxProps={"withinPortal": False},
            )
        ),
    ],
)
