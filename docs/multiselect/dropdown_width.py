import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Your favorite libraries",
    placeholder="Pick values",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    comboboxProps={"position": "bottom-start", "width": 200},
)
