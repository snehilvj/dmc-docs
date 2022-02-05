import dash
import dash_mantine_components as dmc
from dash import html, dcc
from dash_iconify import DashIconify

from lib.blocks import TableOfContents, Heading, Paragraph

dash.register_page(
    __name__,
    "/",
    description="Dash Mantine Components is an extensive UI components library for Plotly Dash with over 55 "
    "components and supports dark theme natively.",
)

toc = [
    {"text": "Dark Theme", "id": "dark-theme"},
    {"text": "Notifications", "id": "notifications"},
    {"text": "Raise Issue", "id": "raise-issue"},
    {"text": "Support", "id": "support"},
]

options = [{"value": val, "label": val} for val in ["React", "Dash", "Flask", "Vue"]]


banner_layout = html.Div(
    [
        dmc.Paper(
            padding="xl",
            children=[
                dmc.Center(
                    dmc.Group(
                        direction="column",
                        position="center",
                        children=[
                            dmc.Image(src="/assets/logo.png", width=250),
                            html.Div(
                                [
                                    dmc.Text(
                                        """Dash Mantine Components is an extensive dash components library with over 50 
                                    components and supports dark theme natively.""",
                                        align="center",
                                    )
                                ],
                                style={"width": 600},
                            ),
                            dcc.Link(
                                [
                                    dmc.Button("Get Started"),
                                ],
                                href="/getting-started/installation",
                            ),
                        ],
                    )
                )
            ],
        ),
        dmc.Space(h=10),
    ]
)

dark_theme_demo_layout = html.Div(
    [
        Heading("Dark Theme", id="dark-theme"),
        dmc.SimpleGrid(
            breakpoints=[{"maxWidth": 860, "cols": 1}],
            cols=2,
            children=[
                html.Div(
                    [
                        Paragraph(
                            "Mantine provides native dark theme support so does Dash Mantine Components. Flip the "
                            "switch to see dark theme in action. "
                        ),
                        dmc.Switch(label="Enable Dark Theme", id="dark-theme-switch"),
                        dmc.Prism(
                            """import dash_mantine_components as dmc

app.layout = dmc.MantineProvider(
    theme={"colorScheme": "dark"},
    children=[
        # dash children here
    ]
)""",
                            language="python",
                            style={"marginTop": 20, "marginBottom": 20},
                        ),
                        dcc.Link(
                            dmc.Text("More about dark theme here.", color="blue"),
                            href="/components/mantineprovider",
                            className="home-page-buttons",
                        ),
                    ]
                ),
                dmc.MantineProvider(
                    id="theme-demo",
                    children=[
                        dmc.Paper(
                            padding="lg",
                            withBorder=True,
                            children=[
                                dmc.Group(
                                    grow=True,
                                    spacing="xl",
                                    direction="column",
                                    children=[
                                        dmc.Group(
                                            grow=True,
                                            children=[
                                                dmc.DateRangePicker(
                                                    label="Select a range",
                                                    amountOfMonths=2,
                                                    style={},
                                                ),
                                                dmc.DatePicker(
                                                    placeholder="Pick a date",
                                                    label="DatePicker",
                                                    required=True,
                                                    style={},
                                                    value="2022-09-26",
                                                ),
                                            ],
                                        ),
                                        dmc.Group(
                                            grow=True,
                                            children=[
                                                dmc.MultiSelect(
                                                    placeholder="Select frameworks",
                                                    data=options,
                                                    label="Multiselect",
                                                    required=True,
                                                    value=["Dash", "Flask"],
                                                ),
                                                dmc.Select(
                                                    placeholder="Pick one",
                                                    label="Select",
                                                    data=options,
                                                    value="React",
                                                ),
                                            ],
                                        ),
                                        dmc.Space(h=10),
                                        dmc.Slider(
                                            value=69,
                                            labelAlwaysOn=True,
                                        ),
                                        dmc.Center(
                                            [
                                                dmc.Chips(
                                                    data=options,
                                                    variant="outline",
                                                    value="Dash",
                                                )
                                            ]
                                        ),
                                        dmc.Group(
                                            position="center",
                                            children=[
                                                dmc.Switch(
                                                    label="Toggle switch", checked=True
                                                ),
                                                dmc.Checkbox(
                                                    label="I agree to sell my privacy",
                                                    checked=True,
                                                ),
                                            ],
                                        ),
                                        dmc.SegmentedControl(
                                            data=options, value="Vue", fullWidth=True
                                        ),
                                    ],
                                )
                            ],
                        )
                    ],
                ),
            ],
        ),
        dmc.Space(h=10),
    ]
)


notifications_demo_layout = html.Div(
    [
        Heading("Notifications", id="notifications"),
        dmc.SimpleGrid(
            breakpoints=[{"maxWidth": 860, "cols": 1}],
            cols=2,
            children=[
                html.Div(
                    [
                        Paragraph("A fully featured notifications system"),
                        dmc.Group(
                            style={"marginTop": 20, "marginBottom": 20},
                            children=[
                                dmc.Button(
                                    "Default",
                                    variant="outline",
                                    id="default-notification",
                                ),
                                dmc.Button(
                                    "Green with icon",
                                    color="green",
                                    variant="outline",
                                    id="green-icon-notification",
                                ),
                                dmc.Button(
                                    "10 sec timeout",
                                    variant="outline",
                                    color="violet",
                                    id="10-sec-notification",
                                ),
                                dmc.Button(
                                    "Loading state",
                                    variant="outline",
                                    color="orange",
                                    id="orange-loading-notification",
                                ),
                            ],
                        ),
                        dcc.Link(
                            dmc.Text("More about notifications here.", color="blue"),
                            href="/components/notification",
                            className="home-page-buttons",
                        ),
                    ]
                ),
                dmc.Prism(
                    """import dash_mantine_components as dmc
from dash_iconify import DashIconify


@app.callback(
    Output("container", "children"), Input("button", "n_clicks")
)
def show_notifications(n_clicks):
    return dmc.Notification(
        id="notification",
        color="green",
        action="show",
        icon=[DashIconify(icon="radix-icons:check-circled")]
    )""",
                    language="python",
                ),
            ],
        ),
        dmc.Space(h=10),
    ]
)


issue_layout = html.Div(
    [
        dmc.SimpleGrid(
            breakpoints=[{"maxWidth": 860, "cols": 1}],
            cols=2,
            children=[
                html.Div(
                    [
                        Heading("Raise Issue", id="raise-issue"),
                        dmc.Space(h=5),
                        Paragraph(
                            "If you find any issues with any components or the documentation, please create an issue."
                        ),
                        dmc.Group(
                            [
                                html.A(
                                    [
                                        dmc.Button(
                                            "Create Issue for dmc",
                                            variant="outline",
                                            color="dark",
                                            leftIcon=[
                                                DashIconify(
                                                    icon="radix-icons:external-link",
                                                )
                                            ],
                                        ),
                                    ],
                                    href="https://github.com/snehilvj/dash-mantine-components/issues/new",
                                    className="home-page-buttons",
                                ),
                                html.A(
                                    [
                                        dmc.Button(
                                            "Create Issue for docs",
                                            variant="outline",
                                            color="dark",
                                            leftIcon=[
                                                DashIconify(
                                                    icon="radix-icons:file-text",
                                                )
                                            ],
                                        ),
                                    ],
                                    href="https://github.com/snehilvj/dmc-demo/issues/new",
                                    className="home-page-buttons",
                                ),
                            ]
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        Heading("Support", id="support"),
                        dmc.Space(h=5),
                        Paragraph(
                            "Now that you are here, please consider giving **dash-mantine-components** a star on "
                            "GitHub. "
                        ),
                        html.A(
                            [
                                dmc.Button(
                                    "Star Dash Mantine Components on GitHub",
                                    variant="outline",
                                    leftIcon=[
                                        DashIconify(
                                            icon="radix-icons:star",
                                        )
                                    ],
                                ),
                            ],
                            href="https://github.com/snehilvj/dash-mantine-components",
                            className="home-page-buttons",
                        ),
                    ],
                ),
            ],
        ),
        dmc.Space(h=10),
    ]
)


made_with_love_layout = dmc.Center(
    [
        dmc.Group(
            spacing="xs",
            children=[
                dmc.Text("Made with"),
                DashIconify(icon="clarity:heart-line", width=15, color="red"),
                dmc.Text("by Snehil Vijay"),
            ],
        )
    ],
    style={"height": 150},
)


layout = [
    banner_layout,
    dark_theme_demo_layout,
    notifications_demo_layout,
    issue_layout,
    made_with_love_layout,
    TableOfContents(toc),
]
