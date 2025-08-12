import dash_mantine_components as dmc

component = dmc.Autocomplete(
    data=[
        {
            "group": "Data Analysis",
            "items": ["Pandas", "NumPy"],
        },
        {
            "group": "Deep Learning",
            "items": ["TensorFlow", "PyTorch"],
        },
    ],
)
