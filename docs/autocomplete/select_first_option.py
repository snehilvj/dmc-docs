import dash_mantine_components as dmc

component = dmc.Autocomplete(
    label="Select your favorite library",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    placeholder="Pick value or enter anything",
    selectFirstOptionOnChange=True,
    w=200,
)
