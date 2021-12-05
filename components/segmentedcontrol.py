import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

segmentedcontrol = html.Div(
    [
        create_component_title("Segmented Control"),
        dmc.SegmentedControl(
            data=[
                {"value": "react", "label": "React"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "ng", "label": "Angular"},
                {"value": "vue", "label": "Vue"},
            ],
        ),
        dmc.Space(h=20),
        dmc.SegmentedControl(
            fullWidth=True,
            data=[
                {"value": "react", "label": "React"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "ng", "label": "Angular"},
                {"value": "vue", "label": "Vue"},
            ],
        ),
        dmc.Space(h=30),
    ]
)

