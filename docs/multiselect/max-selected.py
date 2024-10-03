import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Select your favorite",
    description="You can select a maximum of 3 frameworks.",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    maxValues=3,
    w=400,
)
