import dash_mantine_components as dmc

component = dmc.Group(
    dmc.Anchor(
        "Refer to mantine.dev for more information.",
        href="https://mantine.dev/theming/mantine-provider/",
        style={"textDecoration": "none"},
    ),
    style={"marginBottom": 10},
)
