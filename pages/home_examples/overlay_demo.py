
from dash import  Input, Output, State, callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify


popover_with_filters = dmc.Stack([
    dmc.Text("Popover"),
    dmc.Popover(
        position="bottom-start",
        shadow="md",
        radius="md",
        children=[
            dmc.PopoverTarget(
                    dmc.Button(
                        "Filters",
                        variant="outline",
                        leftSection=DashIconify(icon="fluent:settings-32-regular"),
                        id="filters-button",
                    ),
            ),
            dmc.PopoverDropdown([
                dmc.Text("Order status", size="md", mb=3),
                dmc.SegmentedControl(
                    data=["In progress", "Delivered"],
                    radius="md",
                    size="md"
                ),
                dmc.Text("Brand", size="md", mt="md", mb=5),
                dmc.Checkbox(label="Cannon", size="md", checked=True),
                dmc.Checkbox(label="Nikon", size="md", checked=True, mt=8),
                dmc.Checkbox(label="Sony", size="md", mt=8),
                dmc.Checkbox(label="Fuji", size="md", mt=8),
                dmc.Checkbox(label="Leica", size="md", mt=8),
                dmc.Text("Price range", size="md", mt=24, mb=5),
                dmc.RadioGroup(
                    value="200",
                    children=dmc.Stack([
                        dmc.Radio(label="Less than $100", value="100", size="md"),
                        dmc.Radio(label="$100 - $200", value="200", size="md"),
                        dmc.Radio(label="$200 - $500", value="500", size="md"),
                        dmc.Radio(label="$500 - $1000", value="1000", size="md"),
                        dmc.Radio(label="More than $1000", value="1001", size="md"),
                    ], gap=8),
                ),
            ])
        ]
    )
])

hover_card = dmc.Stack([
    dmc.Text("Hover card"),
    dmc.HoverCard(
        width=320,
        shadow="md",
        withArrow=True,
        openDelay=200,
        closeDelay=400,
        position="bottom-start",
        arrowOffset=15,
        radius="md",
        children=[
            dmc.HoverCardTarget(
                dmc.Card(dmc.Group([
                    dmc.Avatar(src="https://avatars.githubusercontent.com/u/79146003?s=200&v=4", radius="xl"),
                    dmc.Stack([
                        dmc.Text("Mantine", size="sm", fw=700, lh=1, c="bright"),
                        dmc.Anchor("documentation", href="https://mantine.dev/", size="xs", c="dimmed", lh=1)
                    ], gap=5)
                ], style={"width": "max-content"}), withBorder=True),
            ),
            dmc.HoverCardDropdown([
                dmc.Group([
                    dmc.Avatar(src="https://avatars.githubusercontent.com/u/79146003?s=200&v=4", radius="xl"),
                    dmc.Stack([
                        dmc.Text("Mantine", size="sm", fw=700, lh=1, c="bright"),
                        dmc.Anchor("documentation", href="https://mantine.dev/", size="xs", c="dimmed", lh=1)
                    ], gap=5)
                ]),
                dmc.Text("DMC is based on the React Mantine components and hooks library with focus on usability, accessibility and developer experience", size="sm", mt="md"),

            ])
        ]
    )
])

tooltip = dmc.Stack([
    dmc.Text("Tooltip", mt="lg"),
    dmc.Tooltip(
        label="Tooltip",
        withArrow=True,
        children=dmc.Badge("Hover me to see a tooltip", size="lg", variant="dot", color="yellow")
    )
])


modal_and_Drawer_buttons = dmc.Stack([
    dmc.Text("Modal and Drawer", mt="lg"),
    dmc.Group([
        dmc.Button("Open modal", id="open-modal-btn", variant="default", radius="md"),
        dmc.Button("Open drawer", id="open-drawer-btn", variant="default", radius="md")
    ])
])

floating_tooltip = dmc.Stack([
    dmc.Text("FloatingTooltip"),
    dmc.FloatingTooltip(
        label="Tooltip",
        color="orange",
        withinPortal=False,
        children=[
            dmc.Center(
                dmc.Text("Hover over the box to see tooltip"),
                style={
                    "height": 100,
                    "padding": 20,
                    "background-color": "var(--my-light-dark-gray-background)"
                },
            )
        ],
    )
])

authentication = dmc.Card(
    [
        dmc.Text("Welcome! login with:", size="lg"),
        dmc.Group(
            [
                dmc.Button(
                    leftSection=DashIconify(icon="logos:google"),
                    variant="outline",
                ),
                dmc.Button(
                    "BlueSky",
                    leftSection=DashIconify(icon="logos:bluesky"),
                    variant="outline",
                ),
            ],
            grow=True,
            my="lg",
        ),
        dmc.Divider(
            label="Or continue with email",
            variant="dashed",
            labelPosition="center",
        ),
        dmc.Stack(
            [
                dmc.TextInput(label="Email:"),
                dmc.PasswordInput(label="Password:"),
            ],
            gap="md",
        ),
        dmc.Group(
            [
                dmc.Anchor(
                    dmc.Text("Don't have an account? Register", c="gray", size="sm"),
                    href="/",
                ),
                dmc.Button("Login"),
            ],
            grow=True,
            mt="lg",
        ),
    ],
    withBorder=True,
    p="lg",
    w=400,
    h=400,
)


component = dmc.Card([
    # Modal and Drawer overlays
    dmc.Modal(
        id="auth-modal",
        title="Authenticate",
        radius="md",
        children=authentication
    ),

    dmc.Drawer(
        id="auth-drawer",
        title="Authenticate",
        radius="md",
        offset=5,
        children=authentication
    ),

    dmc.Grid([
        dmc.GridCol(
            [popover_with_filters, tooltip],
            span=4
        ),
        dmc.GridCol(
            [hover_card, modal_and_Drawer_buttons],
            span=4
        ),
        dmc.GridCol(
            [floating_tooltip],
            span=3
        )
    ])
], withBorder=True)


@callback(Output("auth-modal", "opened"), Input("open-modal-btn", "n_clicks"), prevent_initial_call=True)
def open_modal(n):
    return True

@callback(Output("auth-drawer", "opened"), Input("open-drawer-btn", "n_clicks"), prevent_initial_call=True)
def open_drawer(n):
    return True
