import dash_mantine_components as dmc

style = {
    "border": f"1px solid var(--mantine-primary-color-filled)",
    "textAlign": "center",
}

component = dmc.Box(
    # Wrapper div is added for demonstration purposes only,
    # it is not required in real projects
    dmc.Grid(
        children=[
            dmc.GridCol(dmc.Box("1", style=style), span={"base": 12, "md": 6, "lg": 3}),
            dmc.GridCol(dmc.Box("2", style=style), span={"base": 12, "md": 6, "lg": 3}),
            dmc.GridCol(dmc.Box("3", style=style), span={"base": 12, "md": 6, "lg": 3}),
            dmc.GridCol(dmc.Box("4", style=style), span={"base": 12, "md": 6, "lg": 3}),
        ],
        gutter="xl",
        type="container",
        breakpoints={
            "xs": "100px",
            "sm": "200px",
            "md": "300px",
            "lg": "400px",
            "xl": "500px",
        },
    ),
    style={"resize": 'horizontal', "overflow": 'hidden', "maxWidth": '100%', "margin": 24 },
)
