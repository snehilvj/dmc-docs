import dash_mantine_components as dmc

component = dmc.Select(
    label="Your favorite library",
    placeholder="Pick value",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    comboboxProps={"position": "bottom-start", "width": 200},
)
