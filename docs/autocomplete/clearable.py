import dash_mantine_components as dmc

component = dmc.Autocomplete(
    label="Your favorite library:",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    value="Pandas",
    clearable=True,
    w=200,
)
