from os import environ

import dash
import dash_mantine_components as dmc
import requests
from dash import html
from dash_iconify import DashIconify

from lib.constants import PAGE_TITLE_PREFIX, PRIMARY_COLOR
from lib.directives.toc import TOC


from .home_examples.inputs_demo import component as inputs_demo

dash.register_page(
    __name__,
    "/",
    title=PAGE_TITLE_PREFIX + "Home",
    description="Official documentation and collection of ready-made Plotly Dash Components created using Dash "
    "Mantine Components. Dash Mantine Components is an extensive UI components library for Plotly Dash "
    "with more than 90 components and supports dark theme natively.",
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
                create_title(
                    "Dash Mantine Components",
                    id="features",
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
        dmc.Title("100+ components", order=1),
        dmc.Title("Input components", order=3, my="lg"),
        dmc.Text(
            """            
            DMC includes all the components you need to build polished, accessible forms and control panels-- styled consistently with the Mantine theme including light and dark mode.    Labels, descriptions, and error messages are built in, and can be added with a prop — no extra layout or components required.       
            """,
            my="lg"

        ),
        inputs_demo,

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
        # dmc.Group(
        #     [
        #         dcc.Link(
        #             dmc.Image(
        #                 src="https://avatars.githubusercontent.com/u/14855837?s=200&v=4",
        #                 alt="ascend.io",
        #                 h=85,
        #                 fit="contain",
        #             ),
        #             href="http://www.ascend.io",
        #             target="_blank",
        #         )
        #     ],
        #     justify="center",
        # ),
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
