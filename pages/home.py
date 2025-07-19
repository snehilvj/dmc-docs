from os import environ

import dash
import dash_mantine_components as dmc
import requests
from dash import html
from dash_iconify import DashIconify

from lib.constants import PAGE_TITLE_PREFIX, PRIMARY_COLOR
from lib.directives.toc import TOC


from .home_examples.inputs_demo import component as inputs_demo
from .home_examples.overlay_demo import component as overlay_demo
from .home_examples.nav_demo import component as nav_demo
from .home_examples.light_dark import component as light_dark_demo
from .home_examples.layout_demo import component as layout_demo




dash.register_page(
    __name__,
    "/",
    title=PAGE_TITLE_PREFIX + "Home",
    description="Official documentation and collection of ready-made Plotly Dash Components created using Dash "
    "Mantine Components. Dash Mantine Components is an extensive UI components library for Plotly Dash "
    "with more than 100 components and supports dark theme natively.",
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
                    "Build fully functional, accessible Dash apps faster than ever! Dash Mantine Components includes over 100 customizable components based on the React Mantine library, with consistent styling, theming, and full support for light and dark mode.",
                    ta="center",
                    mt=10,
                    mb=20,
                    mx=20,
                ),
                dmc.Box([
                    dmc.Text("Version Info:", ta="center"),
                    #version-update
                    dmc.Center(dmc.Anchor("dash-mantine-components=2.1.0" , underline=False, href="https://github.com/snehilvj/dash-mantine-components/discussions/categories/releases", target='_blank')),
                    dmc.Center(dmc.Anchor("mantine=8.1.2" , underline=False, href="https://mantine.dev/", target='_blank')),
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
        dmc.Space(h=20),
        dmc.Title("100+ components", order=2),
        dmc.Text(" "),
        dmc.Title("Input components", order=3, my="lg"),
        dmc.Text(
            """   
            From text fields to date pickers and dropdowns, DMC input components share a consistent design,  making it easy to create polished, accessible forms and control panels. Add labels, descriptions, and error messages with props — no extra layout or components required.       
            """,
            my="lg"
        ),
        inputs_demo,

        dmc.Space(h=110),
        dmc.Title("Overlay components", order=3, my="lg"),
        dmc.Text(
            """            
            Overlay components like modals, drawers, tooltips, and more help display extra content, actions, or context without navigating away from the page.
            """,
            my="lg"
        ),
        overlay_demo,

        dmc.Space(h=110),
        dmc.Title("Navigation components", order=3, my="lg"),
        dmc.Text(
            """            
                
            """,
            my="lg"
        ),
        nav_demo,

        dmc.Space(h=110),
        dmc.Title("Layout components", order=3, my="lg"),
        dmc.Text("""

        """),
        layout_demo,

        dmc.Space(h=110),
        dmc.Title("Light Dark Mode", order=3, my="lg"),
        dmc.Text("""
            Add dark theme to your application with just 1 line of code. All components support dark theme out of the box. Try it out by clicking the theme switch in the header.
        """),
        light_dark_demo,




        dmc.Space(h=100),
        create_title("Sponsors", id="sponsors"),
        create_heading(
            dmc.Anchor(
                "Become a sponsor",
                underline=False,
                href="https://github.com/sponsors/snehilvj",
                target="_blank",
            )
        ),

        dmc.Space(h=30),
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
                    gap="xs",
                    children=[
                        dmc.Text("Made with"),
                        DashIconify(icon="akar-icons:heart", width=19, color="red"),
                        dmc.Text("by Snehil Vijay"),
                    ],
                    justify="center",
                )
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
