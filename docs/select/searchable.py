import dash_mantine_components as dmc

component = dmc.Select(
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    searchable=True,
    w=200,
)
