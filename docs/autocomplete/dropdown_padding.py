import dash_mantine_components as dmc

component = dmc.Paper(
    [
        dmc.Autocomplete(
            label="Zero padding",
            data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
            placeholder="Pick value or enter anything",
            comboboxProps={"dropdownPadding": 0},
            w=400,
        ),
        dmc.Autocomplete(
            label="10px padding",
            data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
            placeholder="Pick value or enter anything",
            comboboxProps={"dropdownPadding": 10},
            w=400,
            mt="md",
        ),
    ]
)
