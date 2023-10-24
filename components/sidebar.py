from dash import clientside_callback, Input, Output
import dash_mantine_components as dmc
from dash_iconify import DashIconify

excluded_links = [
    "/404",
    "/getting-started",
    "/styles-api" ,
    "/style-props",
    "/dash-iconify"
]


def create_main_nav_link(icon, label, href):
    return dmc.Anchor(
        dmc.Group(
            [
                DashIconify(
                    icon=icon, width=23, color=dmc.theme.DEFAULT_COLORS["indigo"][5]
                ),
                dmc.Text(label, size="sm"),
            ]
        ),
        href=href,
        variant="text",
        mb=5,
    )


def create_side_nav_content(nav_data):
    main_links = dmc.Stack(
        spacing="sm",
        mt=20,
        children=[
            create_main_nav_link(
                icon="material-symbols:rocket-launch-rounded",
                label="Getting Started",
                href="/getting-started",
            ),
            create_main_nav_link(
                icon="material-symbols:style",
                label="Styles API",
                href="/styles-api",
            ),
            create_main_nav_link(
                icon="material-symbols:measuring-tape-rounded",
                label="Style Props",
                href="/style-props",
            ),
            create_main_nav_link(
                icon="material-symbols:cookie-rounded",
                label="Dash Iconify",
                href="/dash-iconify",
            ),
        ],
    )

    links = [
        dmc.NavLink(label=entry["name"], href=entry["path"], styles={"root": {"height": 32}})
        for entry in nav_data if entry["path"] not in excluded_links
    ]

    return dmc.Stack(spacing=0, children=[main_links, *links, dmc.Space(h=20)], px=25)


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
                children=create_side_nav_content(nav_data),
            )
        ],
    )


def create_navbar_drawer(nav_data):
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayProps={"opacity": 0.55, "blur": 3},
        zIndex=9,
        size=300,
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                style={"height": "100vh"},
                pt=20,
                children=create_side_nav_content(nav_data),
            )
        ],
    )

clientside_callback(
    """function(n_clicks) { return true }""",
    Output("components-navbar-drawer", "opened"),
    Input("drawer-hamburger-button", "n_clicks"),
    prevent_initial_call=True,
)