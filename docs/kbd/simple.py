import dash_mantine_components as dmc
from dash import html

component = html.Div([dmc.Kbd("⌘"), " + ", dmc.Kbd("shift"), " + ", dmc.Kbd("M")])
