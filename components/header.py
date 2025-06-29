import dash_mantine_components as dmc
from dash import Output, Input, clientside_callback
from dash_iconify import DashIconify


def create_link(icon, href):
    return dmc.Anchor(
        dmc.ActionIcon(
            DashIconify(icon=icon, width=25), variant="transparent", size="lg"
        ),
        href=href,
        target="_blank",
        visibleFrom="xs",
    )


def create_version_menu():
    versions = {
        "1.3.0": "https://dmc-docs-1-3.onrender.com",
        "0.12": "https://dmc-docs-0-12.onrender.com",
        "0.13": "https://dmc-docs-0-13.onrender.com",
    }
    return dmc.Menu(
        [
            dmc.MenuTarget(
                #version-update
                dmc.Button(
                    '2.1',
                    size="xs",
                    leftSection=DashIconify(icon="mingcute:version-fill", width=15),
                )
            ),
            dmc.MenuDropdown(
                [
                    dmc.MenuItem(
                        dmc.Text(name, size="xs"),
                        href=href,
                        target="_blank",
                        leftSection=DashIconify(icon="radix-icons:external-link"),
                    )
                    for name, href in versions.items()
                ],
            ),
        ],
        trigger="hover",
        styles={"item": {"height": 30}},
    )
def search_data(data):
    docs_pages = [
            {"label": component["name"], "value": component["path"]}
            for component in data
            if component["name"] not in ["Home", "Not found 404"]
        ]
    other_search_terms = [
        {"label": "RangeSlider", "value": "/components/slider#range-slider"},
        {"label": "DatePickerInput dates range", "value": "/components/datepickerinput#dates-range"},
        {"label": "CheckboxGroup", "value": "/components/checkbox#checkbox-group-component"},
        {"label": "CheckboxCard", "value": "/components/checkbox#checkboxcad-component"},
        {"label": "ChipGroup", "value": "/components/chip#chipgroups-like-radio-button"},
        {"label": "InlineCodeHighlight", "value": "/components/code-highlight#inline-code"},
        {"label": "CodeHighlightTabs", "value": "/components/code-highlight#with-tabs"},
        {"label": "AvatarGroup", "value": "/components/avatar#avatar-group"},
        {"label": "RadioCard", "value": "/components/radiogroup#radiocard-component"},
        {"label": "AppShellNavbar", "value": "/components/appshell#navbar"},
        {"label": "AppShellHeader", "value": "/components/appshell#header"},
        {"label": "AppShellAside", "value": "/components/appshell#aside"},
        {"label": "AppShellFooter", "value": "/components/appshell#footer"},
        {"label": "AppShellSection", "value": "/components/appshell#section"},
        {"label": "ActionIconGroup", "value": "/components/actionicon#actionicongroup"},
        {"label": "ButtonGroup", "value": "/components/button#button-group"},
    ]
    return docs_pages + other_search_terms


def create_search(data):
    return dmc.Select(
        id="select-component",
        placeholder="Search",
        mt=-2,
        searchable=True,
        clearable=True,
        rightSection=dmc.Kbd("⌘ + k"),
        w=250,
        nothingFoundMessage="Nothing Found!",
        rightSectionWidth=60,
        leftSection=DashIconify(icon="mingcute:search-3-line"),
        data=search_data(data),
        visibleFrom="sm",
        comboboxProps={"shadow": "md"},
    )


theme_toggle = dmc.Switch(
    offLabel=DashIconify(icon="radix-icons:sun", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][8]),
    onLabel=DashIconify(icon="radix-icons:moon", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][6]),
    id="docs-color-scheme-switch",
    persistence=True,
    color="grey",
    size="md"
)

def create_header(data):
    return dmc.AppShellHeader(
        px=25,
        children=[
            dmc.Stack(
                justify="center",
                h=70,
                children=dmc.Grid(
                    justify="space-between",
                    children=[
                        dmc.GridCol(
                            dmc.Group(
                                [
                                    dmc.Anchor(
                                        "DMC", size="xl", href="/", underline=False
                                    ),
                                    create_version_menu(),
                                ]
                            ),
                            span="content",
                        ),
                        dmc.GridCol(
                            span="auto",
                            children=dmc.Group(
                                justify="flex-end",
                                h=31,
                                gap="xl",
                                children=[
                                    create_search(data),
                                    create_link(
                                        "radix-icons:github-logo",
                                        "https://github.com/snehilvj/dash-mantine-components",
                                    ),
                                    create_link(
                                        "bi:discord", "https://discord.gg/KuJkh4Pyq5"
                                    ),
                                    theme_toggle,
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="radix-icons:hamburger-menu",
                                            width=25,
                                        ),
                                        id="drawer-hamburger-button",
                                        variant="transparent",
                                        size="lg",
                                        hiddenFrom="lg",
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

clientside_callback(
    """function(n_clicks) { return true }""",
    Output("components-navbar-drawer", "opened"),
    Input("drawer-hamburger-button", "n_clicks"),
    prevent_initial_call=True,
)
