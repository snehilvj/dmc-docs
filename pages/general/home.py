from os import environ

import dash
import dash_mantine_components as dmc
import requests
from dash import dcc, html
from dash_iconify import DashIconify

from components.toc import create_toc
from lib.constants import PAGE_TITLE_PREFIX, PRIMARY_COLOR

dash.register_page(
    __name__,
    "/",
    title=PAGE_TITLE_PREFIX + "Home",
    description="Official documentation and collection of ready-made Plotly Dash Components created using Dash "
    "Mantine Components. Dash Mantine Components is an extensive UI components library for Plotly Dash "
    "with over 80 components which support dark theme natively.",
)


def create_title(title, id):
    return dmc.Text(title, align="center", weight=300, fz=30, id=id)


def create_heading(text):
    return dmc.Text(text, align="center", mt=10, mb=20, mx=0)


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


def create_tile(icon, heading, description, href):
    return dmc.Card(
        radius="md",
        p="xl",
        withBorder=True,
        m=5,
        children=[
            DashIconify(
                icon=icon,
                height=20,
                color=dmc.theme.DEFAULT_COLORS[PRIMARY_COLOR][5],
            ),
            dmc.Text(heading, size="lg", mt="md"),
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
                    "Give your Dash apps an upgrade with Dash Mantine Components",
                    id="features",
                ),
                create_heading(
                    "With more than 80 components from Mantine React Library"
                ),
                dmc.Group(
                    [
                        dmc.Anchor(dmc.Button("Get Started"), href="/getting-started"),
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
                    mt=80,
                    breakpoints=[
                        {"maxWidth": "xs", "cols": 1},
                        {"maxWidth": "xl", "cols": 2},
                    ],
                    children=[
                        create_tile(
                            icon="akar-icons:calendar",
                            heading="Best DatePickers out there!",
                            description="Easily switch between different years and months while looking great too.",
                            href="/components/datepicker",
                        ),
                        create_tile(
                            icon="uil:paint-tool",
                            heading="Dark Theme Support",
                            description="Use dark theme across all components with no additional steps.",
                            href="/components/mantineprovider",
                        ),
                        create_tile(
                            icon="ph:notification-bold",
                            heading="Notifications System",
                            description="Mantine has a great notifications system, and now you get that in dash apps "
                            "too.",
                            href="/components/notification",
                        ),
                        create_tile(
                            icon="radix-icons:dashboard",
                            heading="Responsive Grid System",
                            description="Design your layouts faster with DMC's Grid and SimpleGrid components.",
                            href="/components/grid",
                        ),
                        create_tile(
                            icon="el:gift",
                            heading="Unique Components",
                            description="Components such as Segmented Control only available with DMC.",
                            href="/components/segmentedcontrol",
                        ),
                        create_tile(
                            icon="lucide:text-cursor-input",
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
        create_heading(
            dmc.Anchor(
                "Become a sponsor",
                underline=False,
                href="https://github.com/sponsors/snehilvj",
                target="_blank",
            )
        ),
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
        create_heading(
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
            h=100,
        ),
        create_toc(
            [
                ("#features", "Features", ""),
                ("#sponsors", "Sponsors", ""),
                ("#contributors", "Contributors", ""),
            ]
        ),
    ]
)
