import dash_mantine_components as dmc

component = dmc.Autocomplete(
    label="Your favorite library:",
    data=[
        {"value":"Pandas"},
        {"value": "NumPy"},
        {"value":"TensorFlow",  "disabled": True},
        {"value":"PyTorch", "disabled": True}
    ],
)
