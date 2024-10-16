import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Select your favorite library",
    placeholder="Select all you like!",
    value=["Pandas", "TensorFlow"],
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    clearable=True,
    w=400,
    mb=180,
)
