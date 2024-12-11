import dash_mantine_components as dmc
from dash import html

component = dmc.Group(
    [
        dmc.Button("Default Button"),
        dmc.Button("Disabled Button", disabled=True, className="dmc-data-attributes-demo"),
        dmc.Button("Loading Button", loading=True, className="dmc-data-attributes-demo"),
        dmc.Button("Button with Left Section", leftSection=html.Div("left"), className="dmc-data-attributes-demo"),
    ],
    gap="sm"
)
