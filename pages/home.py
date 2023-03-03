from os import environ

import dash
import dash_mantine_components as dmc
import requests
from dash import dcc, html
from dash_iconify import DashIconify

from lib.appshell import create_table_of_contents

dash.register_page(
    __name__,
    "/",
    title="Dash Mantine Components",
    description="Official documentation and collection of ready-made Plotly Dash Components created using Dash "
    "Mantine Components. Dash Mantine Components is an extensive UI components library for Plotly Dash "
    "with over 70 components which support dark theme natively.",
)


def create_title(title, id):
    return dmc.Text(title, align="center", style={"fontSize": 30}, id=id)


def create_head(text):
    return dmc.Text(text, align="center", my=10, mx=0)


def create_contributors_avatars():
    resp = requests.get(
        "https://api.github.com/repos/snehilvj/dash-mantine-components/contributors",
        headers={"authorization": f"token {environ['CONTRIB_TOKEN']}"},
    )
    contributors = resp.json()
    children = []
    for user in contributors:
        avatar = dmc.Tooltip(
            dmc.Anchor(dmc.Avatar(src=user["avatar_url"]), href=user["html_url"]),
            label=user["login"],
            position="bottom",
        )
        children.append(avatar)

    return dmc.Group(children, position="center")


def Tile(icon, heading, description, href):
    return dmc.Card(
        radius="md",
        p="xl",
        withBorder=True,
        m=5,
        children=[
            DashIconify(
                icon=icon, height=20, color=dmc.theme.DEFAULT_COLORS["indigo"][5]
            ),
            dmc.Text(heading, size="lg", mt="md"),
            dmc.Divider(
                style={"width": 50},
                size="sm",
                color=dmc.theme.DEFAULT_COLORS["indigo"][5],
                my=10,
            ),
            dmc.Text(description, size="sm", color="dimmed", mt="sm"),
        ],
    )


layout = html.Div(
    [
        dmc.Container(
            size="lg",
            mt=30,
            children=[
                create_title(
                    "Give Your Dash Apps an Upgrade with Dash Mantine Components",
                    id="features",
                ),
                create_head("With more than 70 components from Mantine React Library"),
                dmc.Group(
                    [
                        dmc.Anchor(
                            dmc.Button("Get Started"),
                            href="/getting-started",
                        ),
                        dmc.Anchor(
                            dmc.Button(
                                "Join Discord",
                                variant="outline",
                                leftIcon=DashIconify(icon="bi:discord", width=20),
                            ),
                            href="https://discord.gg/KuJkh4Pyq5",
                            target="_blank",
                        ),
                        dmc.Anchor(
                            dmc.Button(
                                "Sponsor",
                                variant="outline",
                                color="red",
                                leftIcon=DashIconify(icon="akar-icons:heart", width=19),
                            ),
                            href="https://github.com/sponsors/snehilvj",
                            target="_blank",
                        ),
                    ],
                    position="center",
                    mt=30,
                    mb=90,
                ),
            ],
        ),
        dmc.Container(
            size="lg",
            px=0,
            py=0,
            my=40,
            children=[
                dmc.SimpleGrid(
                    cols=3,
                    mt=100,
                    breakpoints=[
                        {"maxWidth": "xs", "cols": 1},
                        {"maxWidth": "xl", "cols": 2},
                    ],
                    children=[
                        Tile(
                            icon="radix-icons:calendar",
                            heading="Best DatePickers out there!",
                            description="Easily switch between different years and months while looking great too.",
                            href="/components/datepicker",
                        ),
                        Tile(
                            icon="radix-icons:blending-mode",
                            heading="Dark Theme Support",
                            description="Use dark theme across all components with no additional steps.",
                            href="/components/mantineprovider",
                        ),
                        Tile(
                            icon="radix-icons:bell",
                            heading="Notifications System",
                            description="Mantine has a great notifications system, and now you get that in dash apps "
                            "too.",
                            href="/components/notification",
                        ),
                        Tile(
                            icon="radix-icons:dashboard",
                            heading="Responsive Grid System",
                            description="Design your layouts faster with DMC's Grid and SimpleGrid components.",
                            href="/components/grid",
                        ),
                        Tile(
                            icon="radix-icons:star",
                            heading="Unique Components",
                            description="Enhance your apps with components such as Segmented Control only available "
                            "with DMC.",
                            href="/components/segmentedcontrol",
                        ),
                        Tile(
                            icon="radix-icons:text-align-left",
                            heading="Better Inputs",
                            description="Add label, description, errors, etc. easily to all inputs.",
                            href="/components/select",
                        ),
                    ],
                )
            ],
        ),
        dmc.Space(h=20),
        create_title("Sponsors", id="sponsors"),
        create_head(
            dmc.Anchor(
                "Become a sponsor",
                underline=False,
                href="https://github.com/sponsors/snehilvj",
                target="_blank",
            )
        ),
        dmc.Space(h=10),
        dmc.Group(
            [
                dcc.Link(
                    dmc.Image(
                        src="https://avatars.githubusercontent.com/u/14855837?s=200&v=4",
                        alt="ascend.io",
                        height=85,
                        fit="contain",
                    ),
                    href="http://www.ascend.io",
                    target="_blank",
                )
            ],
            position="center",
        ),
        dmc.Space(h=40),
        create_title("Contributors", id="contributors"),
        create_head(
            dmc.Anchor(
                "Become a contributor",
                underline=False,
                href="https://github.com/snehilvj/dash-mantine-components",
                target="_blank",
            )
        ),
        dmc.Space(h=10),
        (create_contributors_avatars() if "CONTRIB_TOKEN" in environ else None),
        dmc.Space(h=40),
        dmc.Center(
            [
                dmc.Group(
                    spacing="xs",
                    children=[
                        dmc.Text("Made with"),
                        DashIconify(icon="akar-icons:heart", width=19, color="red"),
                        dmc.Text("by Snehil Vijay"),
                    ],
                )
            ],
            style={"height": 100},
        ),
        create_table_of_contents(
            [
                ("#features", "Features", ""),
                ("#sponsors", "Sponsors", ""),
                ("#contributors", "Contributors", ""),
            ]
        ),
    ]
)
