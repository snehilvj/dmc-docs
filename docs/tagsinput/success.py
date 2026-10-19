import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Your favorite library:",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    success="Looks good"
)
