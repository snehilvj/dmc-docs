import dash_mantine_components as dmc

component = dmc.Select(
    label="Control check icon",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    value="NumPy",
    checkIconPosition="right",
    dropdownOpened=True,
    w=200,
    pb=150,
    id="select-check-icon"
)
