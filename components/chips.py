import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

chips = html.Div(
    [
        create_component_title("Chips"),
        dmc.Chips(
            color="orange",
            variant="outline",
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            value="vue",
        ),
        dmc.Space(h=20),
        dmc.Chips(
            color="red",
            multiple=True,
            variant="filled",
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            value=["vue", "ng"],
        ),
        dmc.Space(h=30),
    ]
)
