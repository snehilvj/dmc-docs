import dash_mantine_components as dmc
from dash import html

component = html.Div(
    " This is a blue element",
    style={
        "backgroundColor": dmc.DEFAULT_THEME["colors"]["blue"][1],
        "color": dmc.DEFAULT_THEME["colors"]["blue"][9],
        "padding": dmc.DEFAULT_THEME["spacing"]["lg"]
    }
)