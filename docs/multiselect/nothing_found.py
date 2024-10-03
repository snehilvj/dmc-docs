import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Pick your favorite libraries",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    searchable=True,
    nothingFoundMessage="Nothing found...",
    w=400,
)
