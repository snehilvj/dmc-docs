import dash_mantine_components as dmc

initial_values = [
    [
        {"value": "react", "label": "React", "group": "Frameworks"},
        {"value": "ng", "label": "Angular", "group": "Frameworks"},
        {"value": "next", "label": "Next.js", "group": "Frameworks"},
        {"value": "jq", "label": "jQuery", "group": "Frameworks"},
        {"value": "sv", "label": "Svelte", "group": "Libraries"},
        {"value": "dj", "label": "Django", "group": "Libraries"},
        {"value": "fl", "label": "Flask", "group": "Libraries"},
    ],
    [
        {"value": "blitz", "label": "Blitz.js", "group": "Frameworks"},
        {"value": "gatsby", "label": "Gatsby.js", "group": "Frameworks"},
        {"value": "vue", "label": "Vue", "group": "Frameworks"},
        {"value": "rw", "label": "Redwood", "group": "Libraries"},
        {"value": "np", "label": "NumPy", "group": "Libraries"},
    ],
]

component = dmc.TransferList(value=initial_values)
