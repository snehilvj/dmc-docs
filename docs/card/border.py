import dash_mantine_components as dmc
from dash_iconify import DashIconify

# fmt:off
images = [
  dmc.Image(radius="sm", src='https://images.unsplash.com/photo-1449824913935-59a10b8d2000?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=250&q=80'),
  dmc.Image(radius="sm", src='https://images.unsplash.com/photo-1444723121867-7a241cacace9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=250&q=80'),
  dmc.Image(radius="sm", src='https://images.unsplash.com/photo-1444084316824-dc26d6657664?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=250&q=80'),
]
# fmt:on

component = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Group(
                children=[
                    dmc.Text("Review Pictures", weight=500),
                    dmc.ActionIcon(
                        DashIconify(icon="carbon:overflow-menu-horizontal"),
                        color="gray",
                        variant="transparent",
                    ),
                ],
                position="apart",
            ),
            withBorder=True,
            inheritPadding=True,
            py="xs",
        ),
        dmc.Text(
            children=[
                dmc.Text(
                    "200+ images uploaded",
                    color="blue",
                    style={"display": "inline"},
                ),
                " since last visit, review them to select which one should be added to your gallery",
            ],
            mt="sm",
            color="dimmed",
            size="sm",
        ),
        dmc.CardSection(
            dmc.Image(
                src="https://images.unsplash.com/photo-1579263477001-7a703f1974e6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=80",
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
