import dash_mantine_components as dmc
from dash import Output, Input, clientside_callback
from dash_iconify import DashIconify

from lib.constants import PRIMARY_COLOR


def create_home_link(label):
    return dmc.Anchor(label, size="xl", href="/", underline=False)


def create_header_link(icon, href, color=PRIMARY_COLOR):
    return dmc.Anchor(
        dmc.ActionIcon(
            DashIconify(icon=icon, width=23), variant="subtle", size="lg", color=color
        ),
        href=href,
        target="_blank",
    )


def create_header_select(data):
    return dmc.Select(
        id="select-component",
        placeholder="Search",
        mt=-3,
        nothingFound="No match found",
        searchable=True,
        clearable=True,
        rightSection=dmc.Kbd("⌘ + k"),
        w=250,
        rightSectionWidth=60,
        icon=DashIconify(icon="mingcute:search-3-line"),
        data=[
            {"label": component["name"], "value": component["path"]}
            for component in data
            if component["name"] not in ["Home", "Not found 404"]
        ],
    )


def create_version_menu():
    mapping = {"0.12": "http://www.dash-mantine-components.com/0.12/static"}

    return dmc.Menu(
        [
            dmc.MenuTarget(
                dmc.Button(
                    "0.13",
                    size="xs",
                    leftIcon=DashIconify(icon="mingcute:version-fill", width=15),
                )
            ),
            dmc.MenuDropdown(
                [
                    dmc.MenuItem(
                        dmc.Text(name, size="xs"),
                        href=href,
                        target="_blank",
                        icon=DashIconify(icon="radix-icons:external-link"),
                    )
                    for name, href in mapping.items()
                ]
            ),
        ],
        trigger="hover",
        styles={"item": {"height": 30}},
    )


def create_header(data):
    return dmc.Header(
        height=70,
        fixed=True,
        px=25,
        children=[
            dmc.Stack(
                justify="center",
                h=70,
                children=dmc.Grid(
                    children=[
                        dmc.Col(
                            dmc.Group(
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
                                    dmc.MediaQuery(
                                        create_version_menu(),
                                        smallerThan="lg",
                                        styles={"display": "none"},
                                    ),
                                ]
                            ),
                            span="content",
                        ),
                        dmc.Col(
                            span="auto",
                            children=dmc.Group(
                                position="right",
                                align="center",
                                h=31,
                                spacing="xl",
                                children=[
                                    dmc.MediaQuery(
                                        create_header_select(data),
                                        smallerThan="md",
                                        styles={"display": "none"},
                                    ),
                                    create_header_link(
                                        "radix-icons:github-logo",
                                        "https://github.com/snehilvj/dash-mantine-components",
                                    ),
                                    create_header_link(
                                        "bi:discord", "https://discord.gg/KuJkh4Pyq5"
                                    ),
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="radix-icons:blending-mode", width=23
                                        ),
                                        color="yellow",
                                        id="color-scheme-toggle",
                                        size="lg",
                                    ),
                                    dmc.MediaQuery(
                                        dmc.ActionIcon(
                                            DashIconify(
                                                icon="radix-icons:hamburger-menu",
                                                width=18,
                                            ),
                                            id="drawer-hamburger-button",
                                            variant="outline",
                                            size=36,
                                        ),
                                        largerThan="lg",
                                        styles={"display": "none"},
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            )
        ],
    )


clientside_callback(
    """
    function(value) {
        console.log(value)
        if (value) {
            return value
        }
    }
    """,
    Output("url", "href"),
    Input("select-component", "value"),
)

# noinspection PyProtectedMember
clientside_callback(
    """
    function(children) { 
        ethicalads.load();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return null
    }
    """,
    Output("select-component", "value"),
    Input("_pages_content", "children"),
)
