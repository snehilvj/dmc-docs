import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Timeline(
    [
        dmc.TimelineItem(
            dmc.Text("Default Bullet without anything"), title="Default Bullet"
        ),
        dmc.TimelineItem(
            dmc.Text("Default Avatar"), bullet=[dmc.Avatar(radius="xl")], title="Avatar"
        ),
        dmc.TimelineItem(
            dmc.Text("Icon from DashIconify"),
            bullet=[
                DashIconify(
                    icon="charm:rocket",
                )
            ],
            bulletSize=30,
            title="Icon",
        ),
        dmc.TimelineItem(
            dmc.Text("Icon styled with theme colors"),
            bullet=[
                dmc.ThemeIcon(
                    size="md",
                    color="indigo",
                    variant="filled",
                    children=[DashIconify(icon="tabler:photo")],
                    radius="xl"
                )
            ],
            title="ThemeIcon",
        ),
    ],
    active=1,
)
