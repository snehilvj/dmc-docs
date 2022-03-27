from collections import defaultdict

import dash
import dash_mantine_components as dmc
from dash import dcc, html
from dash_iconify import DashIconify


def AppShell(children):
    return dmc.MantineProvider(
        theme={"colorScheme": "light"},
        withGlobalStyles=True,
        withNormalizeCSS=True,
        children=[
            dmc.NotificationsProvider(
                [
                    dmc.Container(
                        fluid=True,
                        p="lg",
                        style={"marginTop": 90},
                        children=[
                            html.Div(
                                id="dummy-container-for-header-select",
                                style={"display": "none"},
                            ),
                            html.Div(
                                id="home-notifications-container",
                                style={"display": "none"},
                            ),
                            page_header(),
                            side_nav(),
                            dmc.Container(
                                p="lg",
                                id="main-content",
                                children=children,
                            ),
                        ],
                    )
                ]
            )
        ],
    )


def page_header():
    return dmc.Header(
        height=70,
        fixed=True,
        p="md",
        children=[
            dmc.Group(
                position="apart",
                style={"marginLeft": 20, "marginRight": 20},
                children=[
                    dmc.Group(
                        [
                            dmc.Image(src="/assets/logo_header.png", width=30),
                            dcc.Link(
                                dmc.Text(
                                    "Dash Mantine Components", color="dark", size="xl"
                                ),
                                href="/",
                                style={"textDecoration": "none"},
                            ),
                            dmc.Badge(
                                dmc.__version__,
                                color="gray",
                                variant="outline",
                                radius="xl",
                            ),
                        ]
                    ),
                    dmc.Group(
                        position="right",
                        children=[
                            html.A(
                                dmc.Button(
                                    dmc.Text(
                                        "Source Code",
                                        color="dark",
                                        weight="lighter",
                                        size="sm",
                                    ),
                                    radius="xl",
                                    variant="light",
                                    color="gray",
                                    rightIcon=[
                                        DashIconify(
                                            icon="radix-icons:github-logo",
                                            color="black",
                                            width=20,
                                        )
                                    ],
                                ),
                                href="https://github.com/snehilvj/dash-mantine-components",
                                className="hide-sm",
                            ),
                            html.A(
                                dmc.Button(
                                    dmc.Text(
                                        "Docs",
                                        color="dark",
                                        weight="lighter",
                                        size="sm",
                                    ),
                                    radius="xl",
                                    variant="light",
                                    color="gray",
                                    rightIcon=[
                                        DashIconify(
                                            icon="radix-icons:github-logo",
                                            color="black",
                                            width=20,
                                        )
                                    ],
                                ),
                                href="https://github.com/snehilvj/dmc-docs",
                                className="hide-sm",
                            ),
                            html.A(
                                dmc.Button(
                                    dmc.Text(
                                        "Discord",
                                        color="dark",
                                        weight="lighter",
                                        size="sm",
                                    ),
                                    radius="xl",
                                    variant="light",
                                    color="gray",
                                    rightIcon=[
                                        DashIconify(
                                            icon="fa-brands:discord",
                                            width=20,
                                            color="#7289da",
                                        )
                                    ],
                                ),
                                href="https://discord.gg/KuJkh4Pyq5",
                                className="hide-sm",
                            ),
                            dmc.Select(
                                id="select-component",
                                style={"width": 300},
                                placeholder="Search",
                                nothingFound="No match found",
                                searchable=True,
                                clearable=True,
                                icon=[DashIconify(icon="radix-icons:magnifying-glass")],
                                data=[
                                    {
                                        "label": component["name"],
                                        "value": component["name"],
                                    }
                                    for component in dash.page_registry.values()
                                    if component["module"] not in ["pages.home"]
                                ],
                            ),
                        ],
                    ),
                ],
            )
        ],
    )


def side_nav():
    sections = defaultdict(list)
    for entry in dash.page_registry.values():
        label = entry["module"].split(".")[1]
        label = (" ".join(label.split("-"))).title()
        sections[label].append((entry["name"], entry["path"]))

    children = []
    for section, pages in sorted(sections.items(), reverse=True):
        if section not in ["Home"]:
            component = dmc.Accordion(
                state={"0": True},
                iconPosition="right",
                icon=[DashIconify(icon="radix-icons:chevron-down")],
                children=[
                    dmc.AccordionItem(
                        label=section,
                        children=[
                            dmc.Group(
                                direction="column",
                                spacing="xs",
                                children=[
                                    dcc.Link(
                                        dmc.Text(name, size="sm", color="gray"),
                                        href=path,
                                        id=name,
                                        style={"textDecoration": "none"},
                                    )
                                    for name, path in pages
                                ],
                            )
                        ],
                    )
                ],
            )
            children.append(component)

    return dmc.Navbar(
        id="components-navbar",
        fixed=True,
        position={"top": 70},
        width={"base": 250},
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                children=children,
            )
        ],
    )
