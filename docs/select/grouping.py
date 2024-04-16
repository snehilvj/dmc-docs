import dash_mantine_components as dmc

component = dmc.Select(
    placeholder="Pick one",
    data=[
        {"value": "rick", "label": "Rick", "group": "Used to be a pickle"},
        {"value": "morty", "label": "Morty", "group": "Never was a pickle"},
        {"value": "beth", "label": "Beth", "group": "Never was a pickle"},
        {"value": "summer", "label": "Summer", "group": "Never was a pickle"},
    ],
    style={"width": 300},
)
