import dash_mantine_components as dmc

component = dmc.Title(
    children = [
        "Title in which you want to ",
        dmc.Text("highlight", span=True, c="blue", inherit=True),
        " something."
    ]
)