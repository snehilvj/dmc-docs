import dash_mantine_components as dmc

component = dmc.Paper([
    dmc.Select(
        label="Option cannot be deselected",
        data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
        placeholder="Pick value",
        value="Pandas",
        allowDeselect=False,
        w=400,
    ),
    dmc.Select(
        label="Option can be deselected",
        description="This is the default behavior, click 'Pandas' in the dropdown",
        data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
        placeholder="Pick value",
        value="Pandas",
        allowDeselect=True,
        w=400,
        mt="md"
    ),
])
