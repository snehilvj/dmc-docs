import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Timeline(
    bulletSize=30,
    children=[
        dmc.TimelineItem(
            dmc.Text("Default Bullet without anything", size="sm", color="dimmed"),
            title="Default Bullet",
        ),
        dmc.TimelineItem(
            dmc.Text("Avatar Picture", size="sm", color="dimmed"),
            bullet=[
                dmc.Avatar(
                    src="https://avatars.githubusercontent.com/u/91216500?v=4",
                    radius="xl",
                    size=30,
                )
            ],
            title="Avatar",
        ),
        dmc.TimelineItem(
            dmc.Text("Icon from DashIconify", size="sm", color="dimmed"),
            bullet=[DashIconify(icon="carbon:rocket", width=20)],
            title="Icon",
        ),
        dmc.TimelineItem(
            dmc.Text("Icon styled with theme colors", size="sm", color="dimmed"),
            bullet=[
                dmc.ThemeIcon(
                    size=30,
                    variant="gradient",
                    gradient={"from": "lime", "to": "cyan"},
                    children=[DashIconify(icon="tabler:photo", width=20)],
                    radius="xl",
                )
            ],
            title="ThemeIcon",
        ),
    ],
    lineWidth=2,
)
