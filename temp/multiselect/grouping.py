import dash_mantine_components as dmc

component = dmc.MultiSelect(
    data=[
        {"value": "rick", "label": "Rick", "group": "Used to be a pickle"},
        {"value": "morty", "label": "Morty", "group": "Never was a pickle"},
        {"value": "summer", "label": "Summer", "group": "Never was a pickle"},
    ],
    style={"width": 400},
)
