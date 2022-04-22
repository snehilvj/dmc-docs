import dash_mantine_components as dmc
from dash import dcc
from dash_iconify import DashIconify


def create_main_nav_link(icon, label, href):
    return dcc.Link(
        dmc.Group(
            [
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=30,
                    radius=30,
                    variant="light",
                ),
                dmc.Text(label, size="sm", color="gray"),
            ]
        ),
        href=href,
        style={"textDecoration": "none"},
    )


def create_nav_link(name, path):
    return dcc.Link(
        dmc.Text(name, size="sm", color="gray"),
        href=path,
        id=name,
        style={"textDecoration": "none"},
    )


component = dmc.Navbar(
    # fixed=True, # uncomment this line if you are using this example in your app
    width={"base": 300},
    height=300,
    children=[
        dmc.ScrollArea(
            offsetScrollbars=True,
            type="scroll",
            children=[
                dmc.Group(
                    direction="column",
                    children=[
                        create_main_nav_link(
                            icon="radix-icons:rocket",
                            label="Getting Started",
                            href="/getting-started",
                        ),
                        create_main_nav_link(
                            icon="radix-icons:iconjar-logo",
                            label="Dash Iconify",
                            href="/dashiconify",
                        ),
                    ],
                ),
                dmc.Divider(style={"marginBottom": 20, "marginTop": 20}),
                dmc.Group(
                    direction="column",
                    children=[
                        create_nav_link("Accordion", "/components/accordion"),
                        create_nav_link("DatePicker", "/components/datepicker"),
                    ],
                ),
            ],
        )
    ],
)
