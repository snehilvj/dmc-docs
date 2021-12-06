import dash_mantine_components as dmc
from dash import html
from utils import create_component_title


select = html.Div(
    [
        create_component_title("Select and Multiselect"),
        dmc.Group(
            [
                dmc.Select(
                    data=[
                        {"value": "react", "label": "React"},
                        {"value": "ng", "label": "Angular"},
                        {"value": "svelte", "label": "Svelte"},
                        {"value": "vue", "label": "Vue"},
                        {"value": "riot", "label": "Riot"},
                        {"value": "next", "label": "Next.js"},
                        {"value": "blitz", "label": "Blitz.js"},
                    ],
                ),
                dmc.MultiSelect(
                    id="multi",
                    data=[
                        {"value": "react", "label": "React"},
                        {"value": "ng", "label": "Angular"},
                        {"value": "svelte", "label": "Svelte"},
                        {"value": "vue", "label": "Vue"},
                        {"value": "riot", "label": "Riot"},
                        {"value": "next", "label": "Next.js"},
                        {"value": "blitz", "label": "Blitz.js"},
                    ],
                    value=["vue", "blitz", "riot"],
                ),
            ]
        ),
        dmc.Space(h=30),
    ]
)
