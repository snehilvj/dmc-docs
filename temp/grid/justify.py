import dash_mantine_components as dmc

from lib.configurator import create_configurator

style = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
    "margin": 2,
}

controls = [
    {
        "property": "justify",
        "component": "Select",
        "data": ["space-between", "space-around", "center", "flex-end", "flex-start"],
        "value": "flex-start",
    },
    {
        "property": "align",
        "component": "Select",
        "data": ["stretch", "center", "flex-end", "flex-start"],
        "value": "stretch",
    },
]

demo = dmc.Grid(
    children=[
        dmc.Col("1", style=style, span=3),
        dmc.Col("2", style={**style, "minHeight": 80}, span=3),
        dmc.Col("3", style={**style, "minHeight": 120}, span=3),
    ],
)

component = create_configurator(demo, controls, center=False)
