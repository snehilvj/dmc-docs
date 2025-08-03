import dash_mantine_components as dmc

component = dmc.Popover(
    width=300,
    position="bottom",
    withArrow=True,
    shadow="md",
    children=[
        dmc.PopoverTarget(dmc.Button("Toggle Popover")),
        dmc.PopoverDropdown(
            dmc.Autocomplete(
                label="Your favorite library",
                placeholder="Pick value or enter anything",
                data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
                comboboxProps={"withinPortal": False},
            )
        ),
    ],
)
