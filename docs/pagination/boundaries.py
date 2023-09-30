import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Pagination(total=20, boundaries=1, value=10),
        dmc.Pagination(total=20, boundaries=2, value=10, my=15),
        dmc.Pagination(total=20, boundaries=3, value=10),
    ]
)
