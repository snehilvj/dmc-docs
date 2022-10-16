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


def create_main_nav_link(icon, label, href):
    return dmc.Anchor(
        dmc.Group(
            [
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=30,
                    radius=30,
                    variant="light",
                ),
                dmc.Text(label, size="sm"),
            ]
        ),
        href=href,
        variant="text",
    )


navbar_icons = {
    "Data Display": "radix-icons:dashboard",
    "Inputs & Buttons": "radix-icons:input",
    "Feedback": "radix-icons:info-circled",
    "Overlay": "radix-icons:stack",
    "Navigation": "radix-icons:hamburger-menu",
    "Typography": "radix-icons:letter-case-capitalize",
    "Layout": "radix-icons:container",
    "Miscellaneous": "radix-icons:mix",
}


def create_header(nav_data):
    return dmc.Header(
        height=70,
        fixed=True,
        px=25,
        children=[
            dmc.Group(
                grow=True,
                position="apart",
                children=[
                    dmc.Stack(
                        [
                            dmc.MediaQuery(
                                create_home_link("Dash Mantine Components"),
                                smallerThan="lg",
                                styles={"display": "none"},
                            ),
                            dmc.MediaQuery(
                                create_home_link("DMC"),
                                largerThan="lg",
                                styles={"display": "none"},
                            ),
                        ],
                        justify="center",
                        style={"height": 70},
                    ),
                    dmc.Group(
                        position="right",
                        spacing="xl",
                        children=[
                            dmc.MediaQuery(
                                dmc.Select(
                                    id="select-component",
                                    style={"width": 250},
                                    placeholder="Search",
                                    nothingFound="No match found",
                                    searchable=True,
                                    clearable=True,
                                    data=[
                                        component["name"]
                                        for component in nav_data
                                        if component["name"]
                                        not in ["Home", "Not found 404"]
                                    ],
                                    icon=DashIconify(
                                        icon="radix-icons:magnifying-glass"
                                    ),
                                ),
                                smallerThan="lg",
                                styles={"display": "none"},
                            ),
                            dmc.MediaQuery(
                                dmc.Group(
                                    [
                                        dmc.Anchor(
                                            dmc.ActionIcon(
                                                DashIconify(
                                                    icon="akar-icons:heart", width=18
                                                ),
                                                variant="outline",
                                                size="lg",
                                            ),
                                            target="_blank",
                                            href="https://github.com/sponsors/snehilvj",
                                        ),
                                        dmc.Anchor(
                                            dmc.ActionIcon(
                                                DashIconify(
                                                    icon="radix-icons:github-logo",
                                                    width=20,
                                                ),
                                                variant="outline",
                                                size="lg",
                                            ),
                                            target="_blank",
                                            href="https://github.com/snehilvj",
                                        ),
                                    ],
                                    spacing="xl",
                                ),
                                smallerThan="sm",
                                styles={"display": "none"},
                            ),
                            dmc.ActionIcon(
                                DashIconify(icon="radix-icons:sun", width=18),
                                variant="outline",
                                size="lg",
                                id="color-scheme-toggle",
                            ),
                            dmc.MediaQuery(
                                dmc.ActionIcon(
                                    DashIconify(
                                        icon="radix-icons:hamburger-menu", width=18
                                    ),
                                    variant="outline",
                                    size="lg",
                                ),
                                largerThan="lg",
                                styles={"display": "none"},
                            ),
                        ],
                    ),
                ],
            )
        ],
    )


def create_side_nave_content(nav_data):
    main_links = dmc.Stack(
        spacing="sm",
        mt=20,
        children=[
            create_main_nav_link(
                icon="radix-icons:rocket",
                label="Getting Started",
                href="/getting-started",
            ),
            create_main_nav_link(
                icon="radix-icons:iconjar-logo",
                label="Dash Iconify",
                href="/dash-iconify",
            ),
        ],
    )
    # create component links
    sections = defaultdict(list)
    for entry in nav_data:
        if "section" in entry and entry["section"] not in ["Getting Started"]:
            sections[entry["section"]].append((entry["name"], entry["path"]))

    links = []
    for section, items in sorted(sections.items()):
        links.append(
            dmc.Divider(
                labelPosition="left",
                label=[
                    DashIconify(
                        icon=navbar_icons[section], width=15, style={"marginRight": 10}
                    ),
                    section,
                ],
                my=20,
            )
        )
        links.extend(
            [
                dmc.Anchor(
                    dmc.Text(name, size="sm"), href=path, id=name, variant="text"
                )
                for name, path in items
            ]
        )

    return dmc.Stack(
        spacing="sm", children=[main_links, *links, dmc.Space(h=20)], px=25
    )


def create_side_navbar(nav_data):
    return dmc.MediaQuery(
        dmc.Navbar(
            id="components-navbar",
            fixed=True,
            position={"top": 70},
            width={"base": 300},
            children=[
                dmc.ScrollArea(
                    offsetScrollbars=True,
                    type="scroll",
                    children=create_side_nave_content(nav_data),
                )
            ],
        ),
        smallerThan="lg",
        styles={"display": "none"},
    )


def create_table_of_contents(toc_items):
    children = []
    for url, name, _ in toc_items:
        children.append(
            dmc.Anchor(
                name,
                style={"textTransform": "capitalize", "textDecoration": "none"},
                href=url,
                size="sm",
                color="gray",
            )
        )

    heading = dmc.Text("Table of Contents", mb=10, weight=500)
    toc = dmc.Stack([heading, *children], spacing=0, px=25, mt=20)

    return dmc.MediaQuery(
        dmc.Aside(
            id="toc-navbar",
            position={"top": 70, "right": 0},
            fixed=True,
            width={"base": 300},
            children=toc,
        ),
        smallerThan=1500,
        styles={"display": "none"},
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
        children=[
            create_header(nav_data),
            create_side_navbar(nav_data),
            page_container,
        ],
    )
