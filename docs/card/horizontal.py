
import dash_mantine_components as dmc

completed = 1887
total = 2334

stats = [
    {"value": 447, "label": "Remaining"},
    {"value": 76, "label": "In progress"},
]

items = [
    dmc.Box([
        dmc.Text(stat["value"]),
        dmc.Text(stat["label"], size="xs", c="dimmed"),
    ])
    for stat in stats
]

component = dmc.Card(
    [
        dmc.CardSection(
            dmc.RingProgress(
                roundCaps=True,
                thickness=6,
                size=150,
                sections=[
                    {
                        "value": (completed / total) * 100,
                        "color": "blue",
                    }
                ],
                label=dmc.Box([
                    dmc.Text(
                        f"{((completed / total) * 100):.0f}%",
                        ta="center",
                        fz="lg",
                    ),
                    dmc.Text(
                        "Completed",
                        ta="center",
                        fz="xs",
                        c="dimmed",
                    ),
                ]),
            ),
            inheritPadding=True,
            px="xs",
            withBorder=True,
        ),
        dmc.CardSection(
            [
                dmc.Text("Project tasks", fz="xl"),
                dmc.Box(
                    [
                        dmc.Text("1887"),
                        dmc.Text("Completed", fz="xs", c="dimmed"),
                    ],
                    mt="xs",
                ),
                dmc.Group(items, mt="sm"),
            ],
            inheritPadding=True,
            px="md",
            withBorder=True,
            ml="lg"
        ),
    ],
    padding="sm",
    withBorder=True,
    orientation="horizontal",
    w=400
)

