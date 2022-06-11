import dash_mantine_components as dmc

component = dmc.Group(
    [
        dmc.Pagination(
            total=20,
            # direction="column",
            # withControls=False,
            # withEdges=False,
            grow=True,
            align="stretch",
            siblings=1,
        ),
        dmc.Pagination(
            total=20,
            # direction="column",
            # withControls=False,
            # withEdges=False,
            grow=True,
            align="stretch",
            siblings=2,
        ),
        dmc.Pagination(
            total=20,
            # direction="column",
            # withControls=False,
            # withEdges=False,
            grow=True,
            align="stretch",
            siblings=3,
        ),
    ]
)
