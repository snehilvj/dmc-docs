import dash_mantine_components as dmc

component = dmc.Select(
    label="Your favorite library:",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    success="Looks good"
)
