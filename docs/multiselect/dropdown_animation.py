import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Your favorite libraries",
    placeholder="Pick values",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    comboboxProps={"transitionProps": {"transition": "pop", "duration": 200}},
)
