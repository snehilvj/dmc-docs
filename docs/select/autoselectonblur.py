import dash_mantine_components as dmc

component = dmc.Select(
    label="Option cannot be deselected",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    placeholder="Pick value",
    autoSelectOnBlur=True,
    w=400,
)

