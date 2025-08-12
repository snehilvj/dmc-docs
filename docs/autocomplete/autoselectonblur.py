import dash_mantine_components as dmc

component = dmc.Autocomplete(
    label="Option cannot be deselected",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    placeholder="Pick value",
    autoSelectOnBlur=True,
    clearable=True,
)

