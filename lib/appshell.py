from collections import defaultdict

import dash_mantine_components as dmc
from dash import Output, Input, clientside_callback, html, dcc, page_container
from dash_iconify import DashIconify


def create_home_link(label):
    return dmc.Anchor(
        label,
        size="xl",
        href="/",
        underline=False,
    )


def create_github_button():
    return dmc.MediaQuery(
        dmc.Anchor(
            dmc.Button(
                "Github",
                variant="outline",
                leftIcon=DashIconify(icon="radix-icons:github-logo", width=18),
            ),
            href="https://github.com/sponsors/snehilvj",
        ),
        smallerThan="sm",
        styles={"display": "none"},
    )


def create_sponsor_button():
    return dmc.MediaQuery(
        dmc.Anchor(
            dmc.Button(
                "Sponsor",
                variant="outline",
                color="red",
                leftIcon=DashIconify(icon="akar-icons:heart", width=18),
            ),
            href="https://github.com/sponsors/snehilvj",
        ),
        smallerThan="sm",
        styles={"display": "none"},
    )


def create_header(nav_data):
    return dmc.Header(
        height=70,
        fixed=True,
        pl=25, pr=25,
        children=[
            dmc.Group(
                grow=True,
                position="apart",
                children=[
                    dmc.Stack(
                        [
                            dmc.MediaQuery(
                                create_home_link("Dash Mantine Components"),
                                smallerThan="md",
                                styles={"display": "none"},
                            ),
                            dmc.MediaQuery(
                                create_home_link("DMC"),
                                largerThan="md",
                                styles={"display": "none"},
                            ),
                        ], justify="center", style={"height": 70}
                    ),
                    dmc.Group(
                        position="right",
                        spacing="xl",
                        children=[
                            # dmc.MediaQuery(
                            #     dmc.Select(
                            #         id="select-component",
                            #         style={"width": 250},
                            #         placeholder="Search",
                            #         nothingFound="No match found",
                            #         searchable=True,
                            #         clearable=True,
                            #         data=[
                            #             component["name"]
                            #             for component in nav_data
                            #             if component["name"]
                            #             not in ["Home", "Not found 404"]
                            #         ],
                            #         icon=DashIconify(
                            #             icon="radix-icons:magnifying-glass"
                            #         ),
                            #     ),
                            #     smallerThan="sm",
                            #     styles={"display": "none"},
                            # ),
                            create_github_button(),
                            create_sponsor_button(),
                            dmc.Switch(
                                id="color-scheme-toggle",
                                size="lg",
                                radius="sm",
                                offLabel=DashIconify(
                                    icon="radix-icons:sun", width=16
                                ),
                                onLabel=DashIconify(
                                    icon="radix-icons:moon", width=16
                                ),
                            ),
                            dmc.MediaQuery(
                                dmc.ActionIcon(
                                    DashIconify(
                                        icon="radix-icons:hamburger-menu", width=30
                                    ),
                                    id="small-navbar",
                                ),
                                largerThan="sm",
                                styles={"display": "none"},
                            ),
                        ],
                    ),
                ],
            )
        ],
    )


def create_appshell(nav_data):
    return dmc.MantineProvider(
        theme={
            "colorScheme": "light",
            "fontFamily": "'Inter', sans-serif",
            "primaryColor": "indigo",
            "components": {"Button": {"styles": {"root": {"fontWeight": 400}}}},
        },
        withGlobalStyles=True,
        withNormalizeCSS=True,
        children=[create_header(nav_data), page_container],
    )
