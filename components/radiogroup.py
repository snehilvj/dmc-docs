import dash_mantine_components as dmc
from dash import html
from utils import create_component_title


radiogroup = html.Div(
    [
        create_component_title("RadioGroup"),
        dmc.RadioGroup(
            label="Select your favorite framework/library",
            description="This is anonymous",
            error="This is an error message",
            required=True,
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
