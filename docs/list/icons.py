import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.List(
    icon=[
        dmc.ThemeIcon(
            DashIconify(icon="radix-icons:check-circled", width=16),
            radius="xl",
            color="teal",
            size=24,
        )
    ],
    size="sm",
    spacing="sm",
    children=[
        dmc.ListItem("Join our Discord Community."),
        dmc.ListItem("Install python virtual environment."),
        dmc.ListItem(["Install npm dependencies with ", dmc.Code("npm install")]),
        dmc.ListItem(["Add your new component in ", dmc.Code("src/lib/components.")]),
        dmc.ListItem(
            "Raise a PR, including an example to reproduce the changes contributed by the PR.",
            icon=[
                dmc.ThemeIcon(
                    DashIconify(icon="radix-icons:pie-chart", width=16),
                    radius="xl",
                    color="blue",
                    size=24,
                )
            ],
        ),
    ],
)
