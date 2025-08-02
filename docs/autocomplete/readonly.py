import dash_mantine_components as dmc

component = dmc.Autocomplete(
    label="Your favorite library:",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    readOnly=True,
)
