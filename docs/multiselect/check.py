import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Control check icon",
    placeholder="Select all you like!",
    value=["Pandas", "TensorFlow"],
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    w=400,
    mb=180,
  #  dropdownOpened=True,
    checkIconPosition="right",
)
