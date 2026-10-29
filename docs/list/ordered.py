
import dash_mantine_components as dmc

component = dmc.Box(
    [
        dmc.Text("Start from specific number:", c="dimmed"),
        dmc.List(
            [
                dmc.ListItem("This is item #5"),
                dmc.ListItem("This is item #6"),
                dmc.ListItem("This is item #7"),
                dmc.ListItem("This is item #8"),
            ],
            type="ordered",
            start=5,
        ),
        dmc.Text("Reversed numbering:", mt="lg", c="dimmed"),
        dmc.List(
            [
                dmc.ListItem("This is item #3"),
                dmc.ListItem("This is item #2"),
                dmc.ListItem("This is item #1"),
            ],
            type="ordered",
            reversed=True,
        ),
    ]
)

