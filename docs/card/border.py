import dash_mantine_components as dmc
from dash_iconify import DashIconify

urls = [
    "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-1.png",
    "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-2.png",
    "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-3.png",
]

images = [dmc.Image(radius="sm", src=url) for url in urls]

component = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Group(
                children=[
                    dmc.Text("Review Pictures", fw=500),
                    dmc.ActionIcon(
                        DashIconify(icon="carbon:overflow-menu-horizontal"),
                        color="gray",
                        variant="transparent",
                    ),
                ],
                justify="space-between",
            ),
            withBorder=True,
            inheritPadding=True,
            py="xs",
        ),
        dmc.Text(
            children=[
                dmc.Text(
                    "200+ images uploaded",
                    c="blue",
                    style={"display": "inline"},
                ),
                " since last visit, review them to select which one should be added to your gallery",
            ],
            mt="sm",
            c="dimmed",
            size="sm",
        ),
        dmc.CardSection(
            dmc.Image(
                src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-4.png",
                mt="sm",
            ),
        ),
        dmc.CardSection(
            children=[
                dmc.SimpleGrid(cols=3, children=[i for i in images]),
            ],
            inheritPadding=True,
            mt="sm",
            pb="md",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)
