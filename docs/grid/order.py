import dash_mantine_components as dmc

style = {
    "border": f"1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

component = dmc.Grid(
    children=[
        dmc.GridCol(dmc.Box("2", style=style), span=3, order={"base": 2, "sm": 1, "lg": 3}),
        dmc.GridCol(dmc.Box("3", style=style), span=3, order={"base": 3, "sm": 2, "lg": 2}),
        dmc.GridCol(dmc.Box("1", style=style), span=3, order={"base": 1, "sm": 3, "lg": 1}),
    ],
)
