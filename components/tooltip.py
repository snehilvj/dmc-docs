import dash_mantine_components as dmc
from dash import html
from utils import create_component_title

tooltip = html.Div(
    [
        create_component_title("Tooltip"),
        dmc.Tooltip(
            label=" Use this button to save this information in your profile, after that you will be able to access it any time and share it via email.",
            children=[dmc.Button("Button with a tooltip. Hover on it.")],
            wrapLines=True,
            width=220,
            position="right",
        ),
        dmc.Space(h=30),
    ]
)
