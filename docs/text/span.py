import dash_mantine_components as dmc


component = dmc.Box([
    dmc.Text("These two Text components are inline elements ", span=True, bd="1px solid"),
    dmc.Text("and only take up as much space as needed", span=True,  bd="1px solid"),

    dmc.Divider(my="lg"),

    dmc.Text("These two Text components are block elements",  bd="1px solid"),
    dmc.Text("and take up the full width of their container.",  bd="1px solid")
])

