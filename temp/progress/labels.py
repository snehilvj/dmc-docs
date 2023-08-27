import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.Progress(value=75, label="75%", size="xl"),
        dmc.Space(h=20),
        dmc.Progress(
            size="xl",
            sections=[
                {"value": 30, "color": "pink", "label": "Documents"},
                {"value": 30, "color": "grape", "label": "Apps"},
                {"value": 25, "color": "violet", "label": "Other"},
            ],
        ),
    ]
)
