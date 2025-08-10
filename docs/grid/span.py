import dash_mantine_components as dmc

style = {
    "border": f"1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

component = dmc.Grid(
    children=[
        dmc.GridCol(dmc.Box("1", style=style), span={"base": 12, "md": 6, "lg":3}),
        dmc.GridCol(dmc.Box("2", style=style), span={"base": 12, "md": 6, "lg":3}),
        dmc.GridCol(dmc.Box("3", style=style), span={"base": 12, "md": 6, "lg":3}),
        dmc.GridCol(dmc.Box("4", style=style), span={"base": 12, "md": 6, "lg":3}),
    ],
)
