
import dash_mantine_components as dmc

style = {
    "border": "1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

component = dmc.Grid(
    [
        dmc.GridCol(dmc.Box("1", style=style), span=3),
        dmc.GridCol(dmc.Box("2", style=style), span=3),
        dmc.GridCol(dmc.Box("3", style=style), span=3),
        dmc.GridCol(dmc.Box("4", style=style), span=3),
        dmc.GridCol(dmc.Box("5", style=style), span=3),
        dmc.GridCol(dmc.Box("6", style=style), span=3),
        dmc.GridCol(dmc.Box("7", style=style), span=3),
        dmc.GridCol(dmc.Box("8", style=style), span=3),
    ],
    rowGap="xl",
    columnGap="sm",
)

