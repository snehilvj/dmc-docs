import dash_mantine_components as dmc

component = dmc.Autocomplete(
    label="Your favorite library",
    placeholder="Pick value or enter anything",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    autoSelectOnBlur=True,
    clearable=True,
)

