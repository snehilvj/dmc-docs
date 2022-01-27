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
                        padding="lg",
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
                                padding="lg",
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
        padding="md",
        children=[
            dmc.Group(
                position="apart",
                style={"marginLeft": 20, "marginRight": 20},
                children=[
                    dmc.Group(
                        [
                            dcc.Link(
                                dmc.Text(
                                    "Dash Mantine Components", color="blue", size="xl"
                                ),
                                href="/",
                                style={"textDecoration": "none"},
                            ),
                            dmc.Badge(dmc.__version__, color="gray", variant="outline"),
                        ]
                    ),
                    dmc.Group(
                        id="header-right-section",
                        position="right",
                        children=[
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
                            html.A(
                                DashIconify(
                                    icon="radix-icons:github-logo",
                                    color="black",
                                    width=30,
                                    style={
                                        "marginBottom": "-7px",
                                    },
                                ),
                                href="https://github.com/snehilvj/dash-mantine-components",
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
                children=[
                    dmc.AccordionItem(
                        label=section,
                        children=[
                            dmc.Group(
                                direction="column",
                                spacing="xs",
                                children=[
                                    dcc.Link(
                                        dmc.Text(name, size="sm", color="blue"),
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
                style={"height": "calc(100% - 70px)"},
                offsetScrollbars=True,
                children=children,
            )
        ],
    )
