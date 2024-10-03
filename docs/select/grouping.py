import dash_mantine_components as dmc

component = dmc.Select(
    data=[
        {
            "group": "Data Analysis",
            "items": [
                {"value": "Pandas", "label": "Pandas"},
                {"value": "NumPy", "label": "NumPy"},
            ],
        },
        {
            "group": "Deep Learning",
            "items": [
                {"value": "TensorFlow", "label": "TensorFlow"},
                {"value": "PyTorch", "label": "PyTorch"},
            ],
        },
    ],
    w=400,
)
