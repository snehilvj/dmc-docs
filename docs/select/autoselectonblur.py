import dash_mantine_components as dmc

component = dmc.Select(
    label="Your favorite library:",
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    placeholder="Pick value",
    autoSelectOnBlur=True,
    w=400,
)

