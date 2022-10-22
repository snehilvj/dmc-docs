from collections import defaultdict

import dash_mantine_components as dmc
from dash import Output, Input, clientside_callback, html, dcc, page_container, State
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
                                        {
                                            "label": component["name"],
                                            "value": component["path"],
                                        }
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
                                                color="red",
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
                                                variant="default",
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
                                DashIconify(icon="mdi:theme-light-dark", width=18),
                                variant="outline",
                                size="lg",
                                color="yellow",
                                id="color-scheme-toggle",
                            ),
                            dmc.MediaQuery(
                                dmc.ActionIcon(
                                    DashIconify(
                                        icon="radix-icons:hamburger-menu", width=18
                                    ),
                                    id="drawer-hamburger-button",
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
                dmc.Anchor(name, size="sm", href=path, variant="text")
                for name, path in items
            ]
        )

    return dmc.Stack(
        spacing="sm", children=[main_links, *links, dmc.Space(h=20)], px=25
    )


def create_side_navbar(nav_data):
    return dmc.Navbar(
        fixed=True,
        id="components-navbar",
        position={"top": 70},
        width={"base": 300},
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                children=create_side_nave_content(nav_data),
            )
        ],
    )


def create_navbar_drawer(nav_data):
    return dmc.Drawer(
        size=300,
        id="components-navbar-drawer",
        overlayOpacity=0.55,
        overlayBlur=3,
        zIndex=9,
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                style={"height": "100%"},
                pt=20,
                children=create_side_nave_content(nav_data),
            )
        ],
    )


def create_table_of_contents(toc_items):
    children = []
    for url, name, _ in toc_items:
        children.append(
            html.A(
                dmc.Text(name, color="dimmed", size="sm", variant="text"),
                style={"textTransform": "capitalize", "textDecoration": "none"},
                href=url,
            )
        )

    heading = dmc.Text("Table of Contents", mb=10, weight=500)
    toc = dmc.Stack([heading, *children], spacing=4, px=25, mt=20)

    return dmc.Aside(
        position={"top": 70, "right": 0},
        fixed=True,
        id="toc-navbar",
        width={"base": 300},
        zIndex=10,
        children=toc,
    )


def create_appshell(nav_data):
    return dmc.MantineProvider(
        dmc.MantineProvider(
            theme={
                "fontFamily": "'Inter', sans-serif",
                "primaryColor": "indigo",
                "components": {
                    "Button": {"styles": {"root": {"fontWeight": 400}}},
                    "Alert": {"styles": {"title": {"fontWeight": 500}}},
                    "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                },
            },
            inherit=True,
            children=[
                dcc.Store(id="theme-store", storage_type="local"),
                dcc.Location(id="url"),
                create_header(nav_data),
                create_side_navbar(nav_data),
                create_navbar_drawer(nav_data),
                html.Div(
                    dmc.Container(size="lg", pt=90, children=page_container),
                    id="wrapper",
                ),
            ],
        ),
        theme={"colorScheme": "light"},
        id="mantine-docs-theme-provider",
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )


clientside_callback(
    """ function(data) { return data } """,
    Output("mantine-docs-theme-provider", "theme"),
    Input("theme-store", "data"),
)


clientside_callback(
    """function(n_clicks, data) {
        if (data) {
            if (n_clicks) {
                const scheme = data["colorScheme"] == "dark" ? "light" : "dark"
                return { colorScheme: scheme } 
            }
            return dash_clientside.no_update
        } else {
            return { colorScheme: "light" }
        }
    }""",
    Output("theme-store", "data"),
    Input("color-scheme-toggle", "n_clicks"),
    State("theme-store", "data"),
)


# noinspection PyProtectedMember
clientside_callback(
    """ function(children) { return null } """,
    Output("select-component", "value"),
    Input("_pages_content", "children"),
)

clientside_callback(
    """
    function(value) {
        if (value) {
            return value
        }
    }
    """,
    Output("url", "pathname"),
    Input("select-component", "value"),
)


clientside_callback(
    """function(n_clicks) { return true }""",
    Output("components-navbar-drawer", "opened"),
    Input("drawer-hamburger-button", "n_clicks"),
    prevent_initial_call=True,
)
