import dash_mantine_components as dmc

component = dmc.TagsInput(
    data=[
        {"group": "Frontend", "items": ["React", "Angular"]},
        {"group": "Backend", "items": ["Express", "Django"]},
    ],
    w=400,
)
