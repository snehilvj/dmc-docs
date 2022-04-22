import dash_mantine_components as dmc
from dash import html, dcc
from dash_iconify import DashIconify


def create_home_link(label):
    return dmc.Text(
        label,
        size="xl",
        color="gray",
    )


component = dmc.Header(
    height=70,
    # fixed=True, # uncomment this line if you are using this example in your app
    p="md",
    children=[
        dmc.Container(
            fluid=True,
            children=dmc.Group(
                position="apart",
                align="flex-start",
                children=[
                    dmc.Center(
                        dcc.Link(
                            [
                                dmc.MediaQuery(
                                    create_home_link("Dash Mantine Components"),
                                    smallerThan="sm",
                                    styles={"display": "none"},
                                ),
                                dmc.MediaQuery(
                                    create_home_link("DMC"),
                                    largerThan="sm",
                                    styles={"display": "none"},
                                ),
                            ],
                            href="/",
                            style={"paddingTop": 5, "textDecoration": "none"},
                        ),
                    ),
                    dmc.Group(
                        position="right",
                        align="center",
                        spacing="xl",
                        children=[
                            dmc.MediaQuery(
                                dmc.Select(
                                    style={"width": 250},
                                    placeholder="Search",
                                    nothingFound="No match found",
                                    searchable=True,
                                    clearable=True,
                                    icon=[
                                        DashIconify(icon="radix-icons:magnifying-glass")
                                    ],
                                ),
                                smallerThan="md",
                                styles={"display": "none"},
                            ),
                            html.A(
                                dmc.Tooltip(
                                    dmc.ThemeIcon(
                                        DashIconify(
                                            icon="radix-icons:github-logo",
                                            width=22,
                                        ),
                                        radius=30,
                                        size=36,
                                        variant="outline",
                                        color="gray",
                                    ),
                                    label="Source Code",
                                    position="bottom",
                                ),
                                href="https://github.com/snehilvj/dash-mantine-components",
                            ),
                            html.A(
                                dmc.Tooltip(
                                    dmc.ThemeIcon(
                                        DashIconify(
                                            icon="bi:discord",
                                            width=22,
                                        ),
                                        radius=30,
                                        size=36,
                                        variant="outline",
                                    ),
                                    label="Discord",
                                    position="bottom",
                                ),
                                href="https://discord.gg/KuJkh4Pyq5",
                            ),
                        ],
                    ),
                ],
            ),
        )
    ],
)
