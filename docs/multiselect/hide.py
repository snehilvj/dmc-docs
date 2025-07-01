import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Select your favorite libraries",
    placeholder="Select all you like!",
    hidePickedOptions=True,
    value=["Pandas", "TensorFlow"],
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    w=400,
    mb=140,
    dropdownOpened=True,
    comboboxProps={"withinPortal":False}
)
