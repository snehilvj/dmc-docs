import dash_mantine_components as dmc

component = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                height=160,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Norway Fjord Adventures", weight=500),
                dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
            size="sm",
            color="dimmed",
        ),
        dmc.Button(
            "Book classic tour now",
            variant="light",
            color="blue",
            fullWidth=True,
            mt="md",
            radius="md",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)
