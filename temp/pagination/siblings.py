import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Pagination(total=20, siblings=1, page=10),
        dmc.Pagination(total=20, siblings=2, page=10, my=15),
        dmc.Pagination(total=20, siblings=3, page=10),
    ]
)
