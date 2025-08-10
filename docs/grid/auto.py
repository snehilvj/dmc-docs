import dash_mantine_components as dmc

style = {
    "border": f"1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

component = dmc.Grid(
    children=[
        dmc.GridCol(dmc.Box("span=auto", style=style), span="auto"),
        dmc.GridCol(dmc.Box("span=6", style=style), span=6),
        dmc.GridCol(dmc.Box("span=auto", style=style), span="auto"),
    ],
    gutter="xl",
)
