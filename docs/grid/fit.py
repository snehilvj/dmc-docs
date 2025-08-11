import dash_mantine_components as dmc

style = {
    "border": f"1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

component = dmc.Grid(
    children=[
        dmc.GridCol(dmc.Box("content width", style=style), span="content"),
        dmc.GridCol(dmc.Box("2", style=style), span=6),
    ],
    gutter="xl",
)
