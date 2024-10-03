import dash_mantine_components as dmc

component = dmc.Select(
    label="Pick your favorite library",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    searchable=True,
    nothingFoundMessage="Nothing found...",
    w=400,
)
