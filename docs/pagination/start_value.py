import dash_mantine_components as dmc

component = dmc.Stack([
    dmc.Text("Pages 5–15 (startValue=5, total=15)", mb="xs"),
    dmc.Pagination(total=15, startValue=5, value=5),
])

