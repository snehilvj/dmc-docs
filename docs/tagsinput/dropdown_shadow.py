import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Your favorite library",
    placeholder="Pick value",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    comboboxProps={"shadow": "md"},
)
