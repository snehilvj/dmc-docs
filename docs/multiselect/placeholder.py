import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Paper(
    [
        dmc.MultiSelect(
            label="Default Placeholder",
            data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
            placeholder="Pick values",
            value=["Pandas"],
            w=400,
        ),
        dmc.MultiSelect(
            label="Placeholder removed when values are selected",
            data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
            placeholder="Pick values",
            value=["Pandas"],
            className="dmc-docs-demo",
            w=400,
            mt="md",
        ),
    ]
)
