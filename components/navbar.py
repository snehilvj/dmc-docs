from collections import defaultdict

import dash_mantine_components as dmc
from dash_iconify import DashIconify

from lib.constants import PRIMARY_COLOR

excluded_links = [
    "/404",
    "/getting-started",
    "/styles-api",
    "/style-props",
    "/dash-iconify",
    "/",
    "/migration",
]

category_data = {
    "Date Pickers": {"icon": "material-symbols:calendar-clock"},
    "Miscellaneous": {"icon": "material-symbols:extension"},
    "Charts": {"icon": "material-symbols:stacked-bar-chart-rounded"},
    "Overlay": {"icon": "material-symbols:full-coverage-rounded"},
    "Layout": {"icon": "material-symbols:responsive-layout-rounded"},
    "Theming": {"icon": "material-symbols:invert-colors-rounded"},
    "Inputs": {"icon": "material-symbols:trackpad-input-rounded"},
    "Data Display": {"icon": "material-symbols:display-settings-rounded"},
    "Navigation": {"icon": "material-symbols:navigation-rounded"},
    "Feedback": {"icon": "material-symbols:feedback-rounded"},
    "Typography": {"icon": "material-symbols:custom-typography-rounded"},
    "Buttons": {"icon": "material-symbols:buttons-alt-rounded"},
}


def create_main_link(icon, label, href):
    return dmc.Anchor(
        dmc.Group(
            [
                DashIconify(
                    icon=icon,
                    width=23,
                    color=dmc.DEFAULT_THEME["colors"][PRIMARY_COLOR][5],
                ),
                dmc.Text(label, size="sm"),
            ]
        ),
        href=href,
        variant="text",
        mb=5,
        underline=False,
    )


def create_content(data):
    main_links = dmc.Stack(
        gap="sm",
        mt=30,
        children=[
            create_main_link(
                icon="material-symbols:rocket-launch-rounded",
                label="Getting Started",
                href="/getting-started",
            ),
            create_main_link(
                icon="material-symbols:style",
                label="Styles API",
                href="/styles-api",
            ),
            create_main_link(
                icon="material-symbols:measuring-tape-rounded",
                label="Style Props",
                href="/style-props",
            ),
            create_main_link(
                icon="material-symbols:cookie-rounded",
                label="Dash Iconify",
                href="/dash-iconify",
            ),
            create_main_link(
                icon="material-symbols:bookmark-rounded",
                label="Migration Guide",
                href="/migration",
            ),
        ],
    )

    links = defaultdict(list)
    for entry in data:
        if entry["path"] not in excluded_links:
            link = dmc.NavLink(
                label=entry["name"],
                href=entry["path"],
                h=32,
                className="navbar-link",
                pl=30,
            )
            links[entry["category"]].append(link)

    body = []
    for section, items in links.items():
        body.append(
            dmc.Divider(
                label=[
                    DashIconify(icon=category_data[section]["icon"], height=23),
                    dmc.Text(section, ml=5, size="sm"),
                ],
                labelPosition="left",
                mt=40,
                mb=10,
            )
        )
        body += items

    return dmc.ScrollArea(
        offsetScrollbars=True,
        type="scroll",
        style={"height": "100%"},
        children=dmc.Stack(gap=0, children=[main_links, *body], px=25),
    )


def create_navbar(data):
    return dmc.AppShellNavbar(children=create_content(data))


def create_navbar_drawer(data):
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayProps={"opacity": 0.55, "blur": 3},
        zIndex=1500,
        offset=10,
        radius="md",
        withCloseButton=False,
        size="75%",
        children=create_content(data),
        trapFocus=False,
    )
