from os import environ

import dash
import dash_mantine_components as dmc
import requests
from dash import html
from dash_iconify import DashIconify

from lib.constants import PAGE_TITLE_PREFIX, PRIMARY_COLOR, MANTINE_VERSION, DMC_VERSION, LATEST_RELEASE_ENDPOINT
from lib.directives.toc import TOC

dash.register_page(
    __name__,
    "/",
    title=PAGE_TITLE_PREFIX + "Home",
    description="""
    Documentation for Dash Mantine Components, a component library to use with Plotly Dash apps.
    100+ customizable components built on the React Mantine library, with consistent styling, theming, full light/dark mode support, and accessibility out of the box.        
    """,
)


def create_title(title, id):
    return dmc.Text(title, ta="center", fw=300, fz=30, id=id)


def create_heading(text):
    return dmc.Text(text, ta="center", mt=10, mb=20, mx=0)


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

    return dmc.Group(children, justify="center")


def create_tile(icon, heading, description, href):
    return dmc.Anchor(dmc.Card(
        radius="md",
        p="xl",
        withBorder=True,
        m=5,
        className="homepage-tile",
        children=[
            DashIconify(
                icon=icon,
                height=20,
                color=dmc.DEFAULT_THEME["colors"][PRIMARY_COLOR][5],
            ),
            dmc.Text(heading, size="lg", mt="md"),
            dmc.Text(description, size="sm", c="dimmed", mt="sm"),
        ],
    ), href=href, underline = "never", style={"display":"flex", "height": "100%"})



layout = html.Div(
    [
        dmc.Container(
            size="lg",
            mt=30,
            children=[
                dmc.Title(
                    "Dash Mantine Components",
                    id="features",
                    order=1,
                    ta="center",
                    fz=40

                ),
                dmc.Text(
                    "Build feature-rich, accessible Dash apps faster than ever! Dash Mantine Components includes over 100 customizable components based on the React Mantine library, with consistent styling, theming, and full support for light and dark mode.",
                    ta="center",
                    mt=10,
                    mb=20,
                    mx=20,
                ),
                dmc.Box([
                    dmc.Text("Version Info:", ta="center"),
                    #version-update
                    dmc.Center(dmc.Anchor(f"dash-mantine-components={DMC_VERSION}" , underline=False, href=LATEST_RELEASE_ENDPOINT)),
                    dmc.Center(dmc.Anchor(f"mantine={MANTINE_VERSION}" , underline=False, href="https://mantine.dev/", target='_blank')),
                ]),

                dmc.Group(
                    [
                        dmc.Anchor(dmc.Button("Get Started"), href="/getting-started"),
                        dmc.Anchor(
                            dmc.Button(
                                "Join Discord",
                                variant="outline",
                                leftSection=DashIconify(icon="bi:discord", width=20),
                            ),
                            href="https://discord.gg/KuJkh4Pyq5",
                            target="_blank",
                        ),
                        dmc.Anchor(
                            dmc.Button(
                                "Sponsor",
                                variant="outline",
                                color="red",
                                leftSection=DashIconify(
                                    icon="akar-icons:heart", width=19
                                ),
                            ),
                            href="https://github.com/sponsors/snehilvj",
                            target="_blank",
                        ),
                    ],
                    justify="center",
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
                    mt=80,
                    cols={"xs": 1, "sm": 2, "xl": 3},
                    children=[
                        create_tile(
                            icon="akar-icons:calendar",
                            heading="Best DatePickers out there!",
                            description="Easily switch between different years and months while looking great too.",
                            href="/datepickers-overview",
                        ),
                        create_tile(
                            icon="uil:paint-tool",
                            heading="Dark Theme Support",
                            description="Use dark theme across all components with no additional steps.",
                            href="/mantine-api#color-scheme",
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
                            heading="Responsive Layouts",
                            description="Design your layouts faster with components like Grid, SimpleGrid, Group, Stack and AppShell.",
                            href="/layout-overview",
                        ),
                        create_tile(
                            icon="lucide:text-cursor-input",
                            heading="Better Inputs",
                            description="Add label, description, errors, etc. easily to all inputs.",
                            href="/inputs-overview",
                        ),
                        create_tile(
                            icon="el:gift",
                            heading="Unique Components",
                            description=" Start exploring all the components available in DMC today!",
                            href="/",
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
        dmc.Box(
            [
                dmc.Group(
                    gap="xs",
                    children=[
                        dmc.Text("Made with"),
                        DashIconify(icon="akar-icons:heart", width=19, color="red"),
                        dmc.Text("by Snehil Vijay"),
                    ],
                    justify="center",
                ),
                dmc.Group([
                dmc.Text("Lead maintainer: ", span=True),
                dmc.Anchor(
                    "AnnMarieW ",
                    underline=False,
                    href="https://github.com/AnnMarieW",
                    target="_blank",
                )], mt="sm", justify="center")
            ],
            h=100,
        ),
        TOC.render(
            None,
            None,
            "Table of Contents",
            None,
            **{
                "table_of_contents": [
                    (3, "Features", "features"),
                    (3, "Sponsors", "sponsors"),
                    (3, "Contributors", "contributors"),
                ]
            },
        ),
    ]
)