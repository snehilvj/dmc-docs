import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Control check icon",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    value=["Pandas", "NumPy"],
    checkIconPosition="right",
    dropdownOpened=True,
    w=400,
    pb=150,
    id="multi-select-check-icon",
    comboboxProps={"withinPortal": False}

)
