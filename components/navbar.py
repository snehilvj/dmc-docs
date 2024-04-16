import dash_mantine_components as dmc
from dash import clientside_callback, Input, Output
from dash_iconify import DashIconify

excluded_links = [
    "/404",
    "/getting-started",
    "/styles-api",
    "/style-props",
    "/dash-iconify",
    "/",
]


def create_main_link(icon, label, href):
    return dmc.Anchor(
        dmc.Group(
            [
                DashIconify(
                    icon=icon, width=23, color=dmc.DEFAULT_THEME["colors"]["indigo"][5]
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
        mt=20,
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
            dmc.Divider(my=10),
        ],
    )

    links = [
        dmc.NavLink(
            label=entry["name"], href=entry["path"], styles={"root": {"height": 32}}
        )
        for entry in data
        if entry["path"] not in excluded_links
    ]

    return dmc.ScrollArea(
        offsetScrollbars=True,
        type="scroll",
        style={"height": "100%"},
        children=dmc.Stack(gap=0, children=[main_links, *links], px=25),
    )


def create_navbar(data):
    return dmc.AppShellNavbar(children=create_content(data))


def create_navbar_drawer(data):
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayProps={"opacity": 0.55, "blur": 3},
        zIndex=1500,
        pt=20,
        size="100%",
        children=create_content(data),
    )
