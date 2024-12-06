import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Enter tags",
    placeholder="Some tags are disabled",
    data = [
        {"value": "Pandas"},
        {"value": "NumPy"},
        {"value": "TensorFlow", "disabled": True},
        {"value": "PyTorch", "disabled": True},
    ],
    w=400,
)
