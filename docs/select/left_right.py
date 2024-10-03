import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Paper([
    dmc.Select(
        label="Your favorite library",
        data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
        placeholder="Pick values",
        leftSectionPointerEvents="none",
        leftSection=DashIconify(icon="bi-book"),
        w=400,
    ),
    dmc.Select(
        label="Your favorite library",
        data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
        placeholder="Pick values",
        rightSectionPointerEvents="none",
        rightSection=DashIconify(icon="bi-book"),
        w=400,
        mt="md",
    ),
])
