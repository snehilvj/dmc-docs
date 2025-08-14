import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Paper(
    [
        dmc.Autocomplete(
            label="Your favorite library",
            data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
            placeholder="Pick value or enter anythings",
            leftSectionPointerEvents="none",
            leftSection=DashIconify(icon="bi-book"),
        ),
        dmc.Autocomplete(
            label="Your favorite library",
            data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
            placeholder="Pick value or enter anything",
            rightSectionPointerEvents="none",
            rightSection=DashIconify(icon="bi-book"),
            mt="md",
        ),
    ]
)
