import dash_mantine_components as dmc

component = dmc.Select(
    data=[
        {
            "group": "Frontend",
            "items": [
                {"value": "React", "label": "React"},
                {"value": "Angular", "label": "Angular"},
            ],
        },
        {
            "group": "Backend",
            "items": [
                {"value": "Svelte", "label": "Svelte"},
                {"value": "Vue", "label": "Vue"},
            ],
        },
    ],
    w=200,
)
