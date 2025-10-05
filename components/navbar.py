from collections import defaultdict

import dash_mantine_components as dmc
from dash import callback, Input, Output, ALL, callback_context, clientside_callback
from dash_iconify import DashIconify

from lib.constants import PRIMARY_COLOR

excluded_links = [
    "/404",
    "/getting-started",
    "/mantine-api",
    "/",
    "/help-center",
    "/llms"
]

category_data = {
    "Date Pickers": {"icon": "material-symbols:calendar-clock"},
    "Miscellaneous": {"icon": "material-symbols:extension"},
    "Charts": {"icon": "material-symbols:stacked-bar-chart-rounded"},
    "Overlay": {"icon": "material-symbols:full-coverage-rounded"},
    "Layout": {"icon": "material-symbols:responsive-layout-rounded"},
    "Theming": {"icon": "material-symbols:invert-colors-rounded"},
    "Styling": {"icon": "material-symbols:palette"},
    "Inputs": {"icon": "material-symbols:trackpad-input-rounded"},
    "Data Display": {"icon": "material-symbols:display-settings-rounded"},
    "Navigation": {"icon": "material-symbols:navigation-rounded"},
    "Feedback": {"icon": "material-symbols:feedback-rounded"},
    "Typography": {"icon": "material-symbols:custom-typography-rounded"},
    "Buttons": {"icon": "material-symbols:buttons-alt-rounded"},
    "Combobox": {"icon": "material-symbols:chevron-left-rounded"},
    "Dash": {"icon":"simple-icons:plotly"},
    "Releases": {"icon": "tabler:tag"}
}


def create_main_link(icon, label, href, id):
    return dmc.NavLink(
        leftSection=DashIconify(
            icon=icon,
            width=23,
            color=dmc.DEFAULT_THEME["colors"][PRIMARY_COLOR][6],
        ),
        label=label,
        href=href,
        id=id,
        active="exact"
    )


def create_content(data, idtype):
    main_links = dmc.Stack(
        mt="md",
        gap=0,
        children=[
            create_main_link(
                icon="material-symbols:rocket-launch-rounded",
                label="Getting Started",
                href="/getting-started",
                id={"type": idtype, "index": "/getting-started"},
            ),
            create_main_link(
                icon="material-symbols:style",
                label="Mantine Overview",
                href="/mantine-api",
                id={"type": idtype, "index": "/mantine-api"},
            ),
            create_main_link(
                icon="material-symbols:info-rounded",
                label="Help Center",
                href="/help-center",
                id={"type": idtype, "index": "/help-center"},
            ),
            create_main_link(
                icon="material-symbols:auto-awesome-rounded",
                label="LLMs",
                href="/llms",
                id={"type": idtype, "index": "/llms"},
            ),
            dmc.Anchor("Mantine V8 docs", href="https://mantine.dev/", target="_blank", ml="lg", pt="md"),

        ],
    )

    links = defaultdict(list)
    # note - to set order of links in each category, use the order prop in
    #        the .md page metadata
    for entry in data:
        if entry["path"] not in excluded_links:
            link = dmc.NavLink(
                label=entry["name"],
                href=entry["path"],
                h=32,
                className="navbar-link",
                pl=30,
                id={"type": idtype, "index": entry["path"]},
                active="exact"
            )
            links[entry["category"]].append(link)

    body = []

    # set the order of the categories in the sidebar
    category_order = [
        "Theming",
        "Styling",
        "Layout",
        "Inputs",
        "Combobox",
        "Buttons",
        "Navigation",
        "Feedback",
        "Overlay",
        "Data Display",
        "Typography",
        "Miscellaneous",
        "Date Pickers",
        "Charts",
        "Dash",
        "Releases"
    ]
    sorted_links = {key: links[key] for key in category_order if key in links}

    for section, items in sorted_links.items():
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
        children=dmc.Stack(gap=0, children=[main_links, *body, dmc.Space(h=90)], pl="xs"),
    )


def create_navbar(data):
    return dmc.AppShellNavbar(children=create_content(data, "navlink_navbar"))


def create_navbar_drawer(data):
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayProps={"opacity": 0.55, "blur": 3},
        offset=10,
        radius="md",
        withCloseButton=False,
        size=350,
        children=create_content(data, "navlink_drawer"),
        trapFocus=False,
    )
