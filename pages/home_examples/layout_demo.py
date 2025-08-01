import dash_mantine_components as dmc

def box(label):
    return dmc.Card(
        label,
        shadow="xs",
        withBorder=True,
        ta="Center",
        p="xs"
    )

component = dmc.Card(
        [

            dmc.Text([
                dmc.Anchor("Use AppShell ", href="/components/appshell"),
                "to make an app with a responsive header, navbar, aside and footer"
            ], span=True, my="lg"),
            dmc.Divider(my="md"),
            dmc.Space(h=30),
            dmc.Text("Use Grid if you need columns with different sizes"),
            dmc.Grid([
                dmc.GridCol(box("1"), span=2),
                dmc.GridCol(box("2"), span=4),
                dmc.GridCol(box("3"), span=6),
            ], gutter="md"),

            dmc.Space(h=30),
            dmc.Text("Use SimpleGrid if you need columns with equal size"),
            dmc.SimpleGrid(
                cols=3,
                spacing="md",
                children=[box(str(i)) for i in range(1, 7)],
            ),

            dmc.Space(h=30),
            dmc.Text("Use Stack  to place items vertically"),
            dmc.Stack(
                gap="sm",
                children=[box(f"Row {i}") for i in range(1, 4)],
            ),

            dmc.Space(h=30),
            dmc.Text("Use Group to place items horizontally"),
            dmc.Group(
                gap="md",
                children=[box(str(i)) for i in range(1, 4)],
            ),

            dmc.Space(h=30),
            dmc.Text("Use Flex to create both horizontal and vertical flexbox layouts"),
            dmc.Flex(
                gap="md",
                justify="center",
                wrap="wrap",
                children=[box(str(i)) for i in range(1, 6)],
            ),
            dmc.Flex(
                gap="md",
                justify="center",
                wrap="wrap",
                direction="column",
                align="center",
                children=[box("1"), box("2")],
                mt="md"
            )
        ],
    withBorder=True
    )

