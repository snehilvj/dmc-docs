import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Your favorite library",
    placeholder="Pick values",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    comboboxProps={"transitionProps": {"transition": "pop", "duration": 200}},
)
